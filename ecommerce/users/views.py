from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages 
from django.contrib.auth.models import User 
from .forms import SignUpForm 
from django import forms 



def user_register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Account creato con successo!")
            return redirect('/') 
        else:
            messages.error(request, "C'è stato un problema con la tua registrazione")
            
            return render(request, 'users/register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'users/register.html', {'form': form})



def user_login(request): 
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid(): 
                login(request, form.get_user())
                messages.success(request, "Hai effettuato il login")
                return redirect('/')
        else: 
             messages.success(request, "Lo user non esiste")
             return redirect('login')
    else: 
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form':form})
            

def user_logout(request): 
     logout(request)
     return redirect('/')