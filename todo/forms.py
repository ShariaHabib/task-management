from django.forms import ModelForm,inlineformset_factory
from .models import Task, Photo
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput



# from django.forms import ModelForm, inlineformset_factory

# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'due_date', 'priority', 'complete']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        # images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class PhotoForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(),
    )
    class Meta:
        model = Photo
        fields = ("image",)

# TaskPhotoFormSet = inlineformset_factory(Task, Photo, form=PhotoForm, extra=1)


        
        
class UsercreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
