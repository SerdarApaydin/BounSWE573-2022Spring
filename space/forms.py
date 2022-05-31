from django import forms
from django.contrib.auth.models import User
from space.models import LearningMaterials, Space

class Space_form(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("name","description","spaceImage")


class Material_form(forms.ModelForm):
    class Meta:
        model=LearningMaterials
        fields=("title","space","sequence","material")