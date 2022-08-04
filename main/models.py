from email.mime import image
import imp
from tkinter import CASCADE
from venv import create
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(null = True, blank = True, upload_to = 'images/')
    title = models.CharField(max_length=200, unique=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Sort post data in decending order
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' | ' + self.author

    def get_absolute_url(self):
        return  reverse('home')
