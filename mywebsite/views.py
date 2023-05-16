from django.shortcuts import render

# Create your views here.
from .forms import CommentForm
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

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)


def categories(request, category):
    posts = Post.objects.filter(
        category__name__contains=category
    ).order_by('-post_date')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, 'categories.html', context)
