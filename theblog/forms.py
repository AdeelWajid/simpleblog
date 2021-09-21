from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        # Styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Story'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        # Styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Story'}),
        }
