from django.core.paginator import Paginator  # Import the Paginator class
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Comment, Vote
from .forms import QuestionForm, AnswerForm, CommentForm
from django.urls import reverse
from django.db.models import Count, Q 

def question_list(request):
    questions = Question.objects.all()  # Get all questions
    paginator = Paginator(questions, 10)  # Show 10 questions per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the questions for the current page
    return render(request, 'forumApp/question_list.html', {'page_obj': page_obj})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.annotate(upvote_count=Count('vote__vote_type', filter=Q(vote__vote_type=True)))  # Count upvotes
    answer_form = AnswerForm()

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST, request.FILES)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect(reverse('forumApp:question_detail', kwargs={'pk': question.pk}))  # Use question.pk for redirect

    return render(request, 'forumApp/question_detail.html', {
        'question': question,
        'answers': answers,
        'answer_form': answer_form
    })

@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            form.save_m2m()  # Save tags
            # Redirect using the reverse URL pattern name
            return redirect(reverse('forumApp:question_detail', kwargs={'pk': question.pk}))
    else:
        form = QuestionForm()
    
    return render(request, 'forumApp/add_question.html', {'form': form})

@login_required
def upvote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    # Check if the user has already voted
    vote, created = Vote.objects.get_or_create(user=request.user, answer=answer, defaults={'vote_type': True})

    if not created:
        # User has already voted; toggle vote if it was a downvote
        if not vote.vote_type:
            vote.vote_type = True  # Change to upvote
            vote.save()

    return redirect('forumApp:question_detail', pk=answer.question.pk)

@login_required
def upvote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.upvotes += 1  # Increment upvote count
    answer.save()
    return redirect('forumApp:question_detail', pk=answer.question.pk)

@login_required
def downvote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.downvotes += 1  # Increment downvote count
    answer.save()
    return redirect('forumApp:question_detail', pk=answer.question.pk)
