from django.db import models

# Create your models here.

class Chore(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    amount = models.IntegerField()

    # override the str method in models to print better
    def __str__(self):
        return self.name

