# forms.py
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'rating', 'img']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'style': 'max-width: 300px;'}),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'style': 'max-width: 300px;'}),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'style': 'max-width: 300px;'}),
            'img': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'style': 'max-width: 300px;'})
        }
