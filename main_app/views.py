from django.shortcuts import render
from .models import Chore


# Build some chores to start

# chores = [
#   {'name': 'Fold the Laundry', 'type': 'cleaning', 'description': 'Folded and put away my clothes today', 'amount': 5},
#   {'name': 'Load Dishwasher', 'type': 'cleaning', 'description': 'I put 4 plates and 2 cups in dishwasher after dinner', 'amount': 3},
# ]

# Create your views here.


# Build the home view
def home(request):
  return render(request, 'home.html')

# About route/page
def about(request):
  return render(request, 'about.html')

# Add the chores index view
def chores_index(request):
  chores = Chore.objects.all()
  return render(request, 'chores/index.html', { 'chores': chores})