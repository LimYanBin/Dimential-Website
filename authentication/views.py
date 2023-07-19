from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Profile


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
            #message.send()

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
                return redirect(reverse('myApp'))
            else :
                messages.success(request, ('There was an error logging'))
                return redirect('loginPage')

        context = {}
        return render(request, 'loginPage.html', context)

def logoutUser(request) :
    logout(request)
    return redirect('loginPage')

@csrf_exempt
@login_required(login_url='loginPage')
def edit_profile(request) :

    if request.method=='POST' :

        username = request.POST['username']
        oldpass = request.POST['oldpass']
        newpass1 = request.POST['newpass1']
        newpass2 = request.POST['newpass2']
        user = User.objects.get (id=request.user.id)

        if username == request.user.username :
            pass

        else :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')

            else :
                user.username = username
                user.save()
                messages.info(request, 'Username had changed to ' +username)
                return redirect('edit_profile')
            
        #not empty    
        if len(oldpass.strip()) & len(newpass1.strip()) & len(newpass2.strip()) :
            if (oldpass == oldpass) & (newpass1 == newpass2):
                messages.info(request, 'Password had changed successfully')

            else :
                messages.info(request, 'Invalid action')
        else :
            messages.info(request, 'Invalid action')


    context = {}
    return render(request, 'edit_profile.html', context)

@csrf_exempt
@login_required(login_url='loginPage')
def edit_profile_image(request) :
    form =ImageForm(request.POST, request.FILES, instance=request.user.profile)

    if request.method=='POST' :

        if form.is_valid() :
            form.save()
            return redirect('edit_profile')

    context = {'form': form}
    return render(request, 'edit_profile_image.html', context)







