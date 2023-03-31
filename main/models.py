from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=225, unique=True)
    image = models.ImageField(upload_to='blog_images/')
    content = RichTextField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    # Sort post data in descending order
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} : {self.author}'

    def get_absolute_url(self):
        return reverse('home')
