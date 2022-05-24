from django import forms
from django.contrib.auth.models import User
from space.models import LearningMaterials

class Material_form(forms.ModelForm):
    class Meta:
        model=LearningMaterials
        fields=("title","space","sequence","material")