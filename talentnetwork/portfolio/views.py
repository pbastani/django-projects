from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, DetailView, ListView
from datetime import datetime

from .forms import \
    RegisterForm, \
    LoginForm, \
    UploadPhotosForm, \
    EditProfileForm, \
    EditPhotoForm
from portfolio.models import Profile, Photo

import pdb
# pdb.set_trace()


@login_required()
def follow(request, username=""):
    me = request.user
    user = User.objects.filter(username=username).first()
    if not user:
        return HttpResponseRedirect(reverse('portfolio:home'))

    profile = user.profile
    follower = profile.followers.filter(user=me).first()
    if not follower:
        user.profile.followers.add(me.profile)
        me.profile.followees.add(user.profile)

    return HttpResponseRedirect(reverse('portfolio:user_profile', kwargs={'username': username}))


def user_profile(request, username=""):
    me = request.user
    user = User.objects.filter(username=username).first()
    profile = user.profile
    follower = profile.followers.filter(user=me).first()

    context = {'page_title': "Profile",
               'profile': profile,
               'follower': follower,
               'user': user,
               'me': me}
    return render(request, 'portfolio/user_profile.html', context)


def user_photo(request, username="", position=0):
    me = request.user
    user = User.objects.filter(username=username).first()
    photo = user.photos.filter(position=position).first()

    if "-" in position:
        position = len(user.photos.all())-1
        return HttpResponseRedirect('/portfolio/users/'+user.username+'/photos/'+repr(position))

    if not photo:
        return HttpResponseRedirect('/portfolio/users/'+user.username+'/photos/0')

    page_title = user.first_name + " " + user.last_name + " | Photos"
    context = {'page_title': page_title,
               'photo': photo,
               'user': user,
               'me': me}
    return render(request, 'portfolio/user_photo.html', context)


def user_followers(request, username=""):
    me = request.user
    user = User.objects.filter(username=username).first()
    photos = user.photos
    context = {'page_title': "Profile",
               'photos': photos,
               'user': user,
               'me': me}
    return render(request, 'portfolio/user_followers.html', context)


def user_photos(request, username=""):
    me = request.user
    user = User.objects.filter(username=username).first()
    photos = user.photos
    context = {'page_title': "Profile",
               'photos': photos,
               'user': user,
               'me': me}
    return render(request, 'portfolio/user_photos.html', context)

@login_required()
def browse_users(request):
    me = request.user
    users = User.objects.all()
    context = {'page_title': "Users | Browse",
               'users': users,
               'me': me}
    return render(request, 'portfolio/browse_users.html', context)


@login_required()
def upload_photos(request):
    me = request.user
    if request.method == 'POST':
        photos = me.photos
        photo_list = request.FILES.getlist('photos')
        position = len(photos.all())
        for file in photo_list:
            print("Adding photo #"+repr(position))
            photo = Photo(user=me,
                          file=file, views=0,
                          title="Untitled",
                          upload_date=datetime.now(),
                          position=position)
            photos.add(photo)

            pdb.set_trace()
            position += 1

        return HttpResponseRedirect(reverse('portfolio:home'))
    else:
        form = UploadPhotosForm()

    context = {'form': form,
               'me': me}
    return render(request, 'portfolio/upload_photos.html', context)

@login_required()
def delete_portfolio(request):
    me = request.user
    Photo.objects.filter(user=me).delete()
    return HttpResponseRedirect('/portfolio/')

@login_required()
def delete_photo(request, position=0):
    me = request.user
    me.photos.filter(position=position).delete()
    return HttpResponseRedirect('/portfolio/photos/view')

@login_required()
def edit_photo(request, position=0):
    errors = []
    me = request.user
    photos = me.photos
    photo = photos.filter(position=position).first()

    # for negative indices show the last
    if "-" in position:
        position = len(photos)-1
        return HttpResponseRedirect('/portfolio/photos/edit/'+repr(position))

    # if image is not found show the first image
    if not photo:
        return HttpResponseRedirect('/portfolio/photos/edit/0')

    form = None
    if request.method == 'POST':
        form = EditPhotoForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            photo.title = form_data['title']
            photo.save()
            return HttpResponseRedirect('/portfolio/photos/edit/'+position)
        else:
            errors.append('Form errors encountered.')
    else:
        form = EditPhotoForm()
        context = {'page_title': "Profile | Edit",
                   'errors': errors,
                   'form': form,
                   'photo': photo,
                   'me': me}
        return render(request, 'portfolio/edit_photo.html', context)


@login_required()
def edit_profile(request):
    errors = []
    context = {}
    me = request.user
    profile = Profile.objects.filter(user=me).first()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            profile.aboutme = form_data['aboutme']
            profile.website_url = form_data['website_url']
            profile.website_name = form_data['website_name']
            if request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            errors.append('All fields are required.')
    else:
        form = EditProfileForm()

    context = {'page_title': "Profile | Edit",
               'errors': errors,
               'profile': profile,
               'me': me,
               'form': form}
    return render(request, 'portfolio/edit_profile.html', context)

@login_required()
def my_profile(request):
    me = request.user
    context = {'page_title': "Profile",
               'profile': me.profile,
               'me': me}
    return render(request, 'portfolio/profile.html', context)


@login_required()
def my_photos(request):
    me = request.user
    photos = me.photos
    context = {'page_title': "Profile",
               'photos': photos,
               'me': me}
    return render(request, 'portfolio/photos.html', context)


@login_required()
def my_connections(request):
    me = request.user
    followers = me.profile.followers.all()
    followees = me.profile.followees.all()

    pdb.set_trace()
    context = {'page_title': "Profile",
               'followers': followers,
               'followees': followees,
               'me': me}
    return render(request, 'portfolio/followers.html', context)


def register(request):
    errors = []
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            form_data = register_form.cleaned_data
            first_name = form_data['first_name']
            last_name = form_data['last_name']
            username = form_data['username']
            email = form_data['email']
            password = form_data['password']

            if len(User.objects.filter(email=email)) > 0:
                errors.append('Email address already in use.')
            if len(User.objects.filter(username=username)) > 0:
                errors.append('Username already taken.')
            if not errors:
                me = User.objects.create_user(username, email, password)
                me.first_name = first_name
                me.last_name = last_name
                me.save()
                Profile(user=me).save()
                return HttpResponseRedirect('/portfolio/login/')
        else:
            errors.append('All fields are required.')
    else:
        register_form = RegisterForm(initial={'username': '', 'email': '', 'password': ''})
        user = request.user
        if user.is_authenticated():
            return redirect('/portfolio/')

    context_dict = {'register_form': register_form,
                    'errors': errors,
                    'page_title': "Register"}
    return render(request, 'portfolio/register.html', context_dict)


def signin(request):
    me = request.user
    if me.is_authenticated():
        return HttpResponseRedirect('/portfolio/')
    if request.method == 'POST':
        email = request.POST['email']
        user_by_email = User.objects.filter(email=email)

        if user_by_email.count() == 0:
            return HttpResponse("No user associated with the email address exists.")
        if user_by_email.count() == 1:
            username = user_by_email[0].username
        else:
            return HttpResponse("Multiple users with the same email address exist.")

        password = request.POST['password']
        me = authenticate(username=username, password=password)
        if me:
            if me.is_active:
                login(request, me)
                me.profile.last_online = datetime.today()
                me.save()
                return HttpResponseRedirect('/portfolio/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        logged_in = False
        login_form = LoginForm()
        context_dict = {'login_form': login_form,
                        'logged_in': logged_in,
                        'page_title': "Login"}
        return render(request, 'portfolio/login.html', context_dict)


@login_required()
def signout(request):
    logout(request)
    return HttpResponseRedirect('/portfolio/login')