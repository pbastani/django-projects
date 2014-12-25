from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .forms import \
    SignupForm, \
    SigninForm, \
    EditPostForm

from listings.models import Profile, Post

import pdb


def frontend(request):
    context = {}
    return render(request, 'listings/index.html', context)


@login_required()
def my_posts(request):
    me = request.user
    posts = Post.objects.all().filter(user=me)
    context = {'posts': posts,
               'page_title': "View Post"}
    return render(request, 'listings/admin/my_posts.html', context)


@login_required()
def delete_post(request, post_id=0):
    if int(post_id) > 0:
        post = Post.objects.get(id=int(post_id))
        post.delete()
    return HttpResponseRedirect('/listings/myposts/view/')


@login_required()
def edit_post(request, post_id=0):
    errors = []
    me = request.user
    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            title = form_data['title']
            content = form_data['content']
            post = Post(user=me, title=title, content=content, create_date=datetime.today())

            #if request.FILES:
            #    pictures = request.FILES['picture']
            #    print("****** Read the pictures.")
            #    pdb.set_trace()

            post.save()
            return HttpResponseRedirect('/listings/myposts/view/')
    else:
        form = EditPostForm()
        post = Post()
        if int(post_id) > 0:
            post = Post.objects.get(id=int(post_id))

        context = {'form': form,
                   'post': post,
                   'errors': errors,
                   'page_title': "Add Post"}
        return render(request, 'listings/admin/edit_post.html', context)


def view_category(request, category=""):
    context = {'category': 'General'}
    me = request.user
    return render(request, 'listings/category.html', context)


def home(request):
    context = {}
    me = request.user
    if me.is_authenticated():
        return render(request, 'listings/admin/index.html', context)
    else:
        return HttpResponseRedirect('/listings/frontend/')


def signup(request):
    errors = []
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            display_name = form_data['display_name']
            email = form_data['email']
            password = form_data['password']
            username = email.split("@")

            if len(username) != 2:
                errors.append('Invalid email address.')
            else:
                username = username[0]
                if len(User.objects.filter(email=email)) > 0:
                    errors.append('Email address already in use.')
                if len(User.objects.filter(username=username)) > 0:
                    errors.append('Username already taken.')

            if not errors:
                me = User.objects.create_user(username, email, password)
                me.first_name = display_name
                me.save()
                Profile(user=me).save()
                return HttpResponseRedirect('/listings/signin/')
        else:
            errors.append('Invalid form data submitted.')
    else:
        form = SignupForm(initial={'username': '', 'email': '', 'password': ''})
        user = request.user
        if user.is_authenticated():
            return redirect('/listings/')

    context = {'form': form,
                    'errors': errors,
                    'page_title': "Register"}
    return render(request, 'listings/signup.html', context)


def signin(request):
    errors = []
    me = request.user
    if me.is_authenticated():
        return HttpResponseRedirect('/listings/')
    if request.method == 'POST':
        form = SigninForm(data=request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

            email = form_data['email']
            user_by_email = User.objects.filter(email=email)

            if user_by_email.count() == 0:
                errors.append('Email address not registered.')
            else:
                username = user_by_email[0].username
                password = request.POST['password']
                me = authenticate(username=username, password=password)
                if me:
                    if me.is_active:
                        login(request, me)
                        me.profile.last_online = datetime.today()
                        me.save()
                        return HttpResponseRedirect('/listings/')
                    else:
                        errors.append('Your account is disabled.')
                else:
                    errors.append('Invalid login details.')
        else:
            errors.append('Invalid form data submitted.')
    else:
        logged_in = False
        form = SigninForm()
        context = {'form': form,
                        'logged_in': logged_in,
                        'page_title': "Login"}
        return render(request, 'listings/signin.html', context)


def signout(request):
    pdb.set_trace()
    logout(request)
    return HttpResponseRedirect('/listings/')