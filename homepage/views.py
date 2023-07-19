from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginPage')
def base(request):
    return render(request, 'base.html')

@login_required(login_url='loginPage')
def info(request):
    return render(request, 'info.html')

@login_required(login_url='loginPage')
def education(request):
    return render(request, 'education.html')

@login_required(login_url='loginPage')
def events(request):
    return render(request, 'events.html')

@login_required(login_url='loginPage')
def careevent(request):
    return render(request, 'careevent.html')

@login_required(login_url='loginPage')
def communicationevent(request):
    return render(request, 'communicationevent.html')

@login_required(login_url='loginPage')
def images(request):
    return render(request, 'images.html')

@login_required(login_url='loginPage')
def privacy(request):
    return render(request, 'privacy.html')

@login_required(login_url='loginPage')
def contactpage(request):
    return render(request, 'contactpage.html')

@login_required(login_url='loginPage')
def organization(request):
    return render(request, 'organization.html')
