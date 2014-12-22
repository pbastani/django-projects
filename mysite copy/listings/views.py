from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .forms import \
    SignupForm, \
    SigninForm

from listings.models import Profile

import pdb


def home(request):
    context = {}
    me = request.user
    if me.is_authenticated():
        return render(request, 'listings/admin/blank.html', context)
    else:
        return HttpResponseRedirect('/listings/signin/')


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
            errors.append('Form data is invalid.')
    else:
        form = SignupForm(initial={'username': '', 'email': '', 'password': ''})
        user = request.user
        if user.is_authenticated():
            return redirect('/portfolio/')

    context_dict = {'form': form,
                    'errors': errors,
                    'page_title': "Register"}
    return render(request, 'listings/signup.html', context_dict)


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
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        logged_in = False
        form = SigninForm()
        context_dict = {'form': form,
                        'logged_in': logged_in,
                        'page_title': "Login"}
        return render(request, 'listings/signin.html', context_dict)


@login_required()
def signout(request):
    logout(request)
    return HttpResponseRedirect('/listings/')