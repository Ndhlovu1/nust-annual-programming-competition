from django.shortcuts import render
from .forms import ChatForm
from .models import ChatMessage
from .utils import get_bot_response

def chat_view(request):
    response = None
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            response = get_bot_response(user_message)

            # Save the conversation to the database
            ChatMessage.objects.create(message=user_message, response=response)
    else:
        form = ChatForm()
    return render(request, 'chatbot/chat.html', {'form': form, 'response': response})
