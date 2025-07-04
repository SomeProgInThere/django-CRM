from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest

from .forms import SignupForm, AddRecordForm
from .models import Record

# Create your views here.

def indexPage(request: HttpRequest):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Login successful! Welcome, {username}.')
            return redirect('index')
        else:
            messages.warning(request, 'Login failed! Please try again.')
            return redirect('index')
    
    else:
        return render(request, 'index.html', { 'records': records })


def logoutUser(request: HttpRequest):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('index')


def registerUser(request: HttpRequest):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()    
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            login(request, user)
            messages.success(request, f'Registration successful! Welcome, {username}.')
            return redirect('index')
    
    return render(request, 'register.html', { 'form': form })


def viewRecord(request: HttpRequest, key: int):
    if request.user.is_authenticated:
        record = Record.objects.get(id=key)
        return render(request, 'record.html', { 'record': record })
    
    else:
        messages.warning(request, 'Please login to edit records.')
        return redirect('index')


def deleteRecord(request: HttpRequest, key: int):
    if request.user.is_authenticated:
        record = Record.objects.get(id=key)
        record.delete()
        messages.success(request, 'Record deleted successfully!')

        return redirect('index')
    
    else:
        messages.warning(request, 'Please login to edit records.')
        return redirect('index')


def addRecord(request: HttpRequest):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Added record successfully!')
                return redirect('index')

        return render(request, 'add.html', { 'form': form })
    
    else:
        messages.warning(request, 'Please login to edit records.')
        return redirect('index')
    

def updateRecord(request: HttpRequest, key: int):
    if request.user.is_authenticated:
        currentRecord = Record.objects.get(id=key)
        form = AddRecordForm(request.POST or None, instance=currentRecord)

        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully!')
            return redirect('index')
        
        return render(request, 'update.html', { 'form': form })
    
    else:
        messages.warning(request, 'Please login to edit records.')
        return redirect('index')
