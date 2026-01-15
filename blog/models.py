from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    dateCreate = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    datePublish = models.DateTimeField(blank=True, null=True)
    isPublic = models.BooleanField(default=True)

    def __str__(self):
        return self.title
