from django import forms
from .models import Post


# Create your form here
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'image', 'title', 'content')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title', 'required': 'required'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter post content...', 'required': 'required'}),
        }
