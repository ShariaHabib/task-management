from django.forms import ModelForm,inlineformset_factory
from .models import Task, Photo
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ["user"]

class PhotoForm(forms.ModelForm):
        image = forms.ImageField(
            label="Image",
            widget=forms.ClearableFileInput(),
        )
        class Meta:
            model = Photo
            fields = ("image",)

        
        
class UsercreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
