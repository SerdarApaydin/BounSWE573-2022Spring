from django import forms
from django.contrib.auth.models import User
from space.models import LearningMaterialVideos

class Video_form(forms.ModelForm):
    class Meta:
        model=LearningMaterialVideos
        fields=("title","space","sequence","video")