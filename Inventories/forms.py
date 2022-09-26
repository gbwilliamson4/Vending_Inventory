from django import forms
from .models import *
from django.forms import ModelForm
from django import forms


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


# class Needed_Inventory_Form(ModelForm):
#     required_css_class = 'form-control'
#     item = forms.ModelChoiceField(queryset=Item.objects.order_by('name'))
#
#     class Meta:
#         model = Needed_Inventory
#         fields = ['item']
#         labels = {'item': 'Item Name'}
#
#         # widgets = {
#         #     # 'item': forms.ComboField(),
#         #     'item': forms.Select(attrs={'class': 'form-control'}),
#         # }

class Needed_Inventory_Form(ModelForm):
    class Meta:
        model = Needed_Inventory
        ordering = ['item']
        fields = ('item',)

        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {'item': 'Item Name'}

    def __init__(self):
        super(Needed_Inventory_Form, self).__init__()
        self.fields['item'].queryset = self.fields['item'].queryset.order_by('name')

# class Needed_Inventory_Form(ModelForm):
#     class Meta:
#         model = Needed_Inventory
#         fields = ('item',)
#
#         widgets = {
#             # 'item': forms.ComboField(),
#             'item': forms.Select(attrs={'class': 'form-control'}),
#         }
#
#         labels = {'item': 'Item Name'}
