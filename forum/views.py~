from django.shortcuts import render
from forum.models import Forum, UserProfile, Thread, Post
from forum.forms import RegistrerForm, LoginForm, ProfileForm, ThreadPostForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

from forum.models import Forum

def index(request):
    return render(request, 'index.html',{
        'forum': Forum.objects.all()
    })

def register(request):
    if request.method == "POST":
        form = RegistrerForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.cleaned_data['user']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(user, email, password)

            new_profile = UserProfile(avatar = request.FILES['avatar'], user=new_user)
            new_profile.save()
            user_authenticated = authenticate(username=user, password=password)
            login(request, user_authenticated)

            return HttpResponseRedirect('/')
    else:
        form = RegistrerForm()

    return render(request, 'register.html',{
        "form":form
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            password = form.cleaned_data['password']

            user_authenticated = authenticate(username=user, password=password)
            login(request, user_authenticated)

            return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html',{
        "form":form
    })

@login_required(login_url='/login/')
def profile(request, pk):
    profile = UserProfile.objects.get(user=pk)
    img = None

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.avatar = request.FILES['avatar'];
            profile.save()
    else:
        form = ProfileForm()

    if profile.avatar:
        img = "/media/" + profile.avatar.name
    return render(request, 'profile.html',{
        "form":form, 'img':img
    })

@login_required(login_url='/login/')
def new_thread(request, pk):
    forum = Forum.objects.get(pk=pk)
    if request.method == "POST":
        form = ThreadPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            thread = Thread.objects.create(forum=forum, title=title, creator=request.user)
            Post.objects.create(thread=thread, title=title, body=body, creator=request.user)
            return HttpResponseRedirect(reverse("list_post", args=[thread.pk]))
    else:
        form = ThreadPostForm()

    return render(request, 'new_thread.html',{
        "form":form, 'pk':forum.pk
    })

def list_thread(request, pk):
    threads = Thread.objects.filter(forum=pk).order_by("-created")
    return render(request, 'forum.html',{
        'threads_list': threads,
        'pk': pk
    })

def list_post(request, pk):
    posts = Post.objects.filter(thread=pk).order_by("created")
    thread = Thread.objects.get(pk=pk)
    return render(request, 'thread.html',{
        'posts_list': posts,
        'title': thread.title,
        'media_url': settings.MEDIA_URL ,
        'pk':pk,
        'pkForum': thread.forum
    })

@login_required(login_url='/login/')
def new_reply(request, pk):
    thread = Thread.objects.get(pk=pk)
    if request.method == "POST":
        form = ThreadPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            Post.objects.create(thread=thread, title=title, body=body, creator=request.user)
            return HttpResponseRedirect(reverse("list_post", args=[pk]))
    else:
        form = ThreadPostForm(initial={'title': "Re: " + thread.title})

    return render(request, 'reply.html',{
        "form":form, 'pk':pk
    })
