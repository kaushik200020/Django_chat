# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ChatMessage
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('chat')
    else:
        form = SignUpForm()
    return render(request, 'chat/signup.html', {'form': form})

@login_required
def chat(request):
    users = User.objects.exclude(id=request.user.id)
    messages = ChatMessage.objects.filter(receiver=request.user) | ChatMessage.objects.filter(sender=request.user)
    return render(request, 'chat/chat.html', {'users': users, 'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver')
        message = request.POST.get('message')
        receiver = User.objects.get(id=receiver_id)
        ChatMessage.objects.create(sender=request.user, receiver=receiver, message=message)
        return redirect('chat')
