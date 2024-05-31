from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    save_as_draft = forms.BooleanField(
        required=False, widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ['img', 'title', 'content']


class CommentCreateForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control"}
    ))

    class Meta:
        model = Comment
        fields = ('body',)


class CommentEditForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control"}
    ))

    class Meta:
        model = Comment
        fields = ('body',)
