from django import forms
from .models import Post


# Create your form here
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'image', 'content')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title', 'required': 'required'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter post content...', 'required': 'required'}),
        }
