from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required' : '',
            'name' : 'username',
            'id' : 'username',
            'type' : 'text',
            'class' : 'container',
            'placeholder' : 'Username',
            'maxlength' : '16',
        })

        self.fields['email'].widget.attrs.update({
            'required' : '',
            'name' : 'email',
            'id' : 'email',
            'type' : 'email',
            'class' : 'container',
            'placeholder' : 'Email',
        })

        self.fields['password1'].widget.attrs.update({
            'required' : '',
            'name' : 'password1',
            'id' : 'password1',
            'type' : 'password',
            'class' : 'container',
            'placeholder' : 'Password',
        })

        self.fields['password2'].widget.attrs.update({
            'required' : '',
            'name' : 'password2',
            'id' : 'password2',
            'type' : 'password',
            'class' : 'container',
            'placeholder' : 'Password',
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


