from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Post(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    dateCreate = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    datePublish = models.DateTimeField(blank=True, null=True)
    isPublic = models.BooleanField(default=True)

    def __str__(self):
        return self.title
