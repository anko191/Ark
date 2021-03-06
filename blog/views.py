from django.shortcuts import render
from django.utils import timezone
from .models import Post
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    return render(request, 'blog/home.html', {'posts':posts})
def pl(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/pl.html')

def tx(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/tx.html')

def phan(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/phan.html',{'posts':posts})
def progress(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/progress.html')

def contact(request):
    return render(request, 'blog/contact.html')
