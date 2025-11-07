from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment, Tag
from blog.forms import CommentForm

def blog_index(request):
    posts = Post.objects.all().order_by('-created')
    context = {
        "posts": posts
    }    
    return render(request, 'blog/index.html', context)

def blog_tag(request, tag):
    posts = Post.objects.filter(
        tags__name__contains=tag
    ).order_by('-created')
    context = {
        "tag": tag,
        "posts": posts
    }
    return render(request, 'blog/tag.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author_name=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, "blog/detail.html", context)