from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from Authentication.models import *
from .forms import *

# Create your views here.
def main(request):
    user = None

    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
        if Account.objects.filter(username=username).exists():
            user = Account.objects.get(username=username)
            
    context = {'posts': list(reversed(Post.objects.all())), 'user': user}

    return render(request, 'core/main.html', context)

def write_post(request):
    user = None

    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
        if Account.objects.filter(username=username).exists():
            user = Account.objects.get(username=username)

    if not user or not user.can_post:
        return redirect('main')


    if request.method == 'POST':
        form = CreatePost(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            public = form.cleaned_data['public']

            post = Post(title=title, content=content, author=user, public=public)
            post.save()
            return redirect('main')
    
    form = CreatePost()

    context = {'form': form}

    return render(request, 'core/write_post.html', context)

def edit_post(request, id):
    user = None

    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
        if Account.objects.filter(username=username).exists():
            user = Account.objects.get(username=username)

    if not user or not user.can_post:
        return redirect('main')

    if not(Post.objects.filter(id=id).exists() and user == Post.objects.get(id=id).author):
        return redirect('main')

    post = Post.objects.get(id=id)

    if request.method == 'POST':
        form = CreatePost(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            public = form.cleaned_data['public']

            post.title = title
            post.content = content
            post.public = public
            post.save()

            return redirect('main')

    form = CreatePost()
    form['title'].initial = post.title
    form['content'].initial = post.content
    form['public'].initial = post.public

    context = {'form': form, 'post': post}

    return render(request, 'core/edit.html', context)

def delete(request, id):
    user = None

    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
        if Account.objects.filter(username=username).exists():
            user = Account.objects.get(username=username)

    if not user or not user.can_post:
        return redirect('main')

    if not(Post.objects.filter(id=id).exists() and user == Post.objects.get(id=id).author):
        return redirect('main')

    post = Post.objects.get(id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('main')

    context = {'text': 'post'}

    return render(request, 'core/delete.html', context)

def post(request, id):
    user = None

    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
        if Account.objects.filter(username=username).exists():
            user = Account.objects.get(username=username)

    if not Post.objects.filter(id=id).exists():
        return redirect('main')

    post = Post.objects.get(id=id)

    if not post.public and not post.author == user:
        return redirect('main')

    if request.method == 'POST':
        form = CreateComment(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            comment = Comment(author=user, post=post, content=content)
            comment.save()
            return redirect(f'../post/{id}')

    form = CreateComment()

    context = {'post': post, 'user': user, 'form': form, 'amt_comments': len(post.comment_set.all())}

    return render(request, 'core/post.html', context)


def delete_comment(request, id):
    user = None

    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
        if Account.objects.filter(username=username).exists():
            user = Account.objects.get(username=username)

    if not user:
        return redirect('main')

    if not(Comment.objects.filter(id=id).exists() and (user == Comment.objects.get(id=id).author or user.can_post)):
        return redirect('main')

    comment = Comment.objects.get(id=id)
    post = comment.post

    if request.method == 'POST':
        comment.delete()
        return redirect(f'../post/{post.id}')

    context = {'text': 'comment'}

    return render(request, 'core/delete.html', context)
