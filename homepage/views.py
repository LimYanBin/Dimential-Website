from django.shortcuts import render
from django.contrib.auth.decorators import login_required

"""
@login_required(login_url='loginPage')
def homePage(request) :

    return render(request, 'homePage.html')
"""

#@login_required(login_url='loginPage')
def base(request):
    return render(request, 'base.html')

def info(request):
    return render(request, 'info.html')

def education(request):
    return render(request, 'education.html')

def events(request):
    return render(request, 'events.html')

def careevent(request):
    return render(request, 'careevent.html')

def communicationevent(request):
    return render(request, 'communicationevent.html')

def images(request):
    return render(request, 'images.html')

def privacy(request):
    return render(request, 'privacy.html')

def contactpage(request):
    return render(request, 'contactpage.html')

def organization(request):
    return render(request, 'organization.html')
