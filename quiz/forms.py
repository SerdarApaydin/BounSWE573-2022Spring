from django import forms
from django.contrib.auth.models import User
from quiz.models import Quiz, Question

class quiz_form(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ("title","description")

class question_form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question","option1","option2","option3","option4","true_answer")
