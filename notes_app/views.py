from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import notes
from django.contrib.auth import logout
from django.db.models import Q

def login_page(request):
    if request.method == 'POST':
        a=request.POST.get('username')
        b=request.POST.get('password')
        c=authenticate(username=a, password=b)
        if c:
            login(request, c)
            return redirect('home')
        else:    
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        a=request.POST.get('username')
        b=request.POST.get('email')
        c=request.POST.get('password')
        User.objects.create_user(username=a, email=b, password=c)
        return redirect('login')
    return render(request, 'register.html')


@login_required
def home(request):
    items=notes.objects.filter(user=request.user)
    query = request.GET.get('search')
    if query:
        items = items.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__icontains=query)
        )
    return render(request, 'home.html' , {'items': items})

@login_required
def create_note(request):
    if request.method == 'POST':
        a=request.POST.get('title')
        b=request.POST.get('content')
        c=request.POST.get('category')
        notes.objects.create(title=a, content=b, category=c, user=request.user)
        return redirect('home')
    return render(request, 'create_note.html')

@login_required
def delete_note(request, id):
    a=notes.objects.get(id=id, user=request.user)
    a.delete()
    return redirect('home')

@login_required
def update_note(request, id):
    a=notes.objects.get(id=id, user=request.user)
    if request.method == 'POST' :
        a.title=request.POST.get('title')
        a.content=request.POST.get('content')
        a.category=request.POST.get('category')
        a.save()
        return redirect('home')
    return render(request, 'update_note.html', {'a': a})    


def logout_user(request):
    logout(request)
    return redirect('login')