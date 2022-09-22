from django import forms
from .models import *
from django.forms import ModelForm


# class Item_Form(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['name', 'total_price', 'quantity']
#         labels = {'name': 'Item Name', 'total_price': 'Total Price', 'quantity': 'Quantity'}


class Item_Form(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'quantity', 'total_price')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01})
        }

        labels = {'name': 'Item Name', 'quantity': 'Quantity', 'total_price': 'Total Price', }
