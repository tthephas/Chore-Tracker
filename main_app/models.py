from django.db import models
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
from django.db.models import F



# Create your models here.
class Chore(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    description = models.TextField(max_length=400)
    amount = models.IntegerField()
  
    
    # override the str method in models to print better
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('chores_detail', kwargs={'chore_id': self.id})



class Parent(models.Model):
    name = models.CharField(max_length=50)
    children = models.IntegerField()
    chores = models.ManyToManyField(Chore)
    # user foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)

        # override the str method in models to print better
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('parents_detail', kwargs={'parent_id': self.id})
    

class Kid(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    # description = models.CharField(max_length=150)
    current_balance = models.IntegerField(default=0)
    # every kid, has one parent
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    chores = models.ManyToManyField(Chore)

    # parent = models.CharField(max_length=150, default='jim')

        # override the str method in models to print better
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('kids_detail', kwargs={'kid_id': self.id})
    
    # func for piggy bank increase
    def add_to_balance(self):
        self.current_balance += 25
        self.save()


class Photo(models.Model):
    url = models.CharField(max_length=200)
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for kid_id: {self.kid_id} @{self.url}"

