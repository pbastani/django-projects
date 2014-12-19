from django.shortcuts import render


def home(request):
    me = request.user
    context = {}
    return render(request, 'listings/index.html', context)