from django import forms
from django.contrib.auth.models import User
from forum.models import Post, Answer

class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","text")

class Answer_form(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("text")
        