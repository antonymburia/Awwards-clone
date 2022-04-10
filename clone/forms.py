from django import forms
from django.contrib.auth.models import User
from .models import User,Profile,Comment,Project
from django.contrib.auth.forms import UserCreationForm

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','project_id']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

