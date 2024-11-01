# archive/views.py
# archive/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Avg
from django.http import FileResponse
from .models import Book, Rating


def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all()
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'archive/book_list.html', {'page_obj': page_obj})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user_rating = book.ratings.filter(user=request.user).first()

    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        Rating.objects.update_or_create(
            book=book,
            user=request.user,
            defaults={'rating': rating_value}
        )
        return redirect('archivesApp:book_detail', pk=book.pk)

    return render(request, 'archive/book_detail.html', {'book': book, 'user_rating': user_rating})

# archive/views.py

@login_required
def download_pdf(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return FileResponse(book.pdf_file.open(), as_attachment=True)

