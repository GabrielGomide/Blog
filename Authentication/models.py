from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    can_post = models.BooleanField()

    def __str__(self):
        return self.username


