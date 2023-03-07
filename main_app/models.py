from django.db import models
from django.urls import reverse

# Create your models here.

class Chore(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    amount = models.IntegerField()

    # override the str method in models to print better
    def __str__(self):
        return self.name
    
    # FIX THIS LATER, detail page needed?
    def get_absolute_url(self):
        return reverse('detail', kwargs={'chore_id': self.id})

