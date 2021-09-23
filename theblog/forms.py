from django import forms
from .models import Post, Category
from ckeditor.fields import RichTextFormField


# choices = Category.objects.all().values_list('name', 'name')
# choice_list = []
# for item in choices:


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet', 'header_image')

        # Styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'value': }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # 'body': RichTextFormField()
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter Category'}),
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
