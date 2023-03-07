from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Chore
from django.views.generic.detail import DetailView


# Build some chores to start

# chores = [
#   {'name': 'Fold the Laundry', 'type': 'cleaning', 'description': 'Folded and put away my clothes today', 'amount': 5},
#   {'name': 'Load Dishwasher', 'type': 'cleaning', 'description': 'I put 4 plates and 2 cups in dishwasher after dinner', 'amount': 3},
# ]

# Create your views here.
class ChoreCreate(CreateView):
  model = Chore
  fields = '__all__'
#   success_url = '/chores/{chore_id}'


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

def chores_detail(request, chore_id):
  chore = Chore.objects.get(id=chore_id)
  return render(request, 'chores/detail.html', { 'chore': chore })