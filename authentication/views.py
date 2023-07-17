from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .tasks import send_email_task as task


#class
from .forms import CreateUserForm 

@csrf_exempt    
def signupPage(request) :
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        email = request.POST['email']
        username = request.POST['username']

        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + username)

            html_template = 'gmail.html'
            html_message = render_to_string(html_template)
            subject = "Welcome to Dementia Malaysia"
            email_from = settings.EMAIL_HOST_USER
            receiver = [email]
            message = EmailMessage(subject, html_message, email_from, receiver)
            message.content_subtype = 'html'
            message.send()

            return redirect('loginPage')
        
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exist')
            return redirect('signupPage')
        
        #elif User.objects.filter(email=email).exists():
        #    messages.info(request, 'Email was already taken!')
        #    return redirect('signupPage')
        
    context = {'form':form}
    return render(request, 'signUp.html', context)

@csrf_exempt
def loginPage(request) :
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('homePage'))
            else :
                messages.success(request, ('There was an error logging'))
                return redirect('loginPage')

        context = {}
        return render(request, 'loginPage.html', context)

def logoutUser(request) :
    logout(request)
    return redirect('loginPage')






