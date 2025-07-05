# notes/models.py
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title