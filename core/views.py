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
            post = Post(title=title, content=content, author=user)
            post.save()
            return redirect('main')
    else:
        form = CreatePost()

    context = {'form': form}

    return render(request, 'core/write_post.html', context)


