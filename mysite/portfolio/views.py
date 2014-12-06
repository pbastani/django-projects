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
from .models import Profile, Photo

import pdb
# pdb.set_trace()


def user_profile(request, username=""):
    user = User.objects.filter(username=username).first()
    profile = Profile.objects.filter(user=user).first()
    context = {'page_title': "Profile",
               'profile': profile,
               'user': user}
    return render(request, 'portfolio/user_profile.html', context)


@login_required()
def find_friends(request):
    users = User.objects.all()
    context = {'page_title': "Friends | Find",
               'users': users}
    return render(request, 'portfolio/find_friends.html', context)


@login_required()
def upload_photos(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    if request.method == 'POST':
        photo_list = request.FILES.getlist('photos')
        position = len(profile.photos.all())
        for file in photo_list:
            print("Adding photo #"+repr(position))
            photo = Photo(profile=profile,
                          file=file, views=0,
                          title="Untitled",
                          upload_date=datetime.now(),
                          position=position)
            profile.photos.add(photo)
            position += 1

        profile.save()
        return HttpResponseRedirect(reverse('portfolio:home'))
    else:
        form = UploadPhotosForm()

    context = {'form': form}
    return render(request, 'portfolio/upload_photos.html', context)

@login_required()
def delete_portfolio(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    photo = Photo.objects.filter(profile=profile).delete()
    return HttpResponseRedirect('/portfolio/')

@login_required()
def delete_photo(request, position=0):
    user = request.user
    portfolio = user.portfolio
    photos = portfolio.photos.all()
    photo = photos.filter(position=position).first()
    Photo.objects.filter(id=photo.id).delete()
    return HttpResponseRedirect('/portfolio/')

@login_required()
def edit_photo(request, position=0):
    errors = []
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    photos = profile.photos.all()
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
                   'photo': photo}
        return render(request, 'portfolio/edit_photo.html', context)


@login_required()
def edit_profile(request):
    errors = []
    context = {}
    user = request.user
    profile = Profile.objects.filter(user=user).first()
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
               'user': user,
               'form': form}
    return render(request, 'portfolio/edit_profile.html', context)


def home(request):
    user = request.user
    if user.is_authenticated():
        profile = Profile.objects.filter(user=user).first()
        context = {'page_title': "Profile",
                   'profile': profile,
                   'user': user}
        return render(request, 'portfolio/index.html', context)
    else:
        return HttpResponseRedirect(reverse('portfolio:login'))


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
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                profile = Profile(user=user)
                profile.save()
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
    user = request.user
    if user.is_authenticated():
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
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
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