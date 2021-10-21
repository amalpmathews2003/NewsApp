from django.db import models

class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.name