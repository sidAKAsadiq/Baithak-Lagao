from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

#from django.contrib.auth.models import User


class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username' , 'email' , 'password1' , 'password2' ]
    

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host' , 'members']

class UserForm(ModelForm):
    class Meta:
        model = User #['username' , 'email']
        fields = ['avatar','username', 'email' , 'bio']