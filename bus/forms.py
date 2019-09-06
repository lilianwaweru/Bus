from django import forms
from .models import Car,Comments


class CarForm(forms.ModelForm):
    class Meta:
        model =  Car
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude =['user']        