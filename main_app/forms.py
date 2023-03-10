# forms.py

from django.forms import ModelForm
from .models import Kid

class KidForm(ModelForm):
  class Meta:
    model = Kid
    fields = ['name', 'age']
