from django.db import models
from django.urls import reverse
from django import forms

# would like a drop down for type, cleaning or learning
# tuple of choices for type of chore
# chore_type = (
#     ('C', 'Cleaning'),
#     ('L', 'Learning')
# )

# Create your models here.

class Kid(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.CharField(max_length=150)

        # override the str method in models to print better
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'kid_id': self.id})

class Chore(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    description = models.TextField(max_length=400)
    amount = models.IntegerField()
    
    

    # override the str method in models to print better
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'chore_id': self.id})

