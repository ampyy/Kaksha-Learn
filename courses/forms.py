from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Name'}), required=True, max_length=50)
    number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder' : "Enter Your Calling Number"}), max_length=10, min_length=10)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write Your Query'}), required=True,
                              max_length=500)

    class Meta:
        model = ContactUs
        fields = ['name', 'number', 'message']


class BoughtForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Name'}), required=True,
                           max_length=50)
    number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder' : "Enter Your Same Calling Number"}),
                             max_length=10, min_length=10)
    paid = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), initial="YES")

    class Meta:
        model =Bought
        fields = ['name', 'number', 'paid']