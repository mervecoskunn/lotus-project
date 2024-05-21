from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    save_as_draft = forms.BooleanField(
        required=False, widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ['img', 'title', 'content']
