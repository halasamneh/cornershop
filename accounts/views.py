from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth.models import Group
# Create your views here.

def home(request):
   return render(request,'home.html')

def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='merchants')
            user.groups.add(group) 
            auth_login(request,user)
            return redirect('home')
            
    return render(request,'signup.html',{'form':form})

