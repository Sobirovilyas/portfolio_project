from django.shortcuts import render


# Create your views here.
from .models import Project, Post, Comment


def index(request):
    return render(request, 'projects.html')


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'project_detail.html', context)


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def blog_index(request):
    posts = Post.objects.all().order_by('-post_date')
    context = {'posts': posts}
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-comment_date')
    context = {'post': post, 'comments': comments}
    return render(request, 'blog_detail.html', context)
