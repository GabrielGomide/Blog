from django.db import models
from Authentication.models import *


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField()
    public = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def break_content(self):
        return self.content.split('\n')


class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.content

    def break_content(self):
        return self.content.split('\n')


