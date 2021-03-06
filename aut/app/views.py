from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def signup(request):
    if request.method =='POST' :
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            usernameu = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username = usernameu, password = password1)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form' : form }
    return render(request,'registration/signup.html', context)