from django.db import models

# Create your models here.


class User(models.Model):
    username = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    password = models.TextField(max_length=200)

    def __str__(self):
        return self.username