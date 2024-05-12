# forms.py
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'rating', 'img']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'price': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'category': forms.Select(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        #     'rating': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'img': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        # }
