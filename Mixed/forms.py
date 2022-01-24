# Copyright Aden Handasyde 2019

from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from Mixed.models import *
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    title = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)


    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'img', 'price', 'stock',)

class QtyForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('stock',)
