from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chore, Kid
from django.views.generic.detail import DetailView


# Build some chores to start

# chores = [
#   {'name': 'Fold the Laundry', 'type': 'cleaning', 'description': 'Folded and put away my clothes today', 'amount': 5},
#   {'name': 'Load Dishwasher', 'type': 'cleaning', 'description': 'I put 4 plates and 2 cups in dishwasher after dinner', 'amount': 3},
# ]

kids = [
  {'name': 'Mya', 'Age': 11, 'description': 'very silly'},
  {'name': 'Ryan', 'Age': 9, 'description': 'very funny'}
]


# Build the home view
def home(request):
  return render(request, 'home.html')

# About route/page
def about(request):
  return render(request, 'about.html')

# Add the kids index view
def kids_index(request):
  kids = Kid.objects.all()
  return render(request, 'kids/index.html', { 'kids': kids })

# Add the chores index view
def chores_index(request):
  chores = Chore.objects.all()
  return render(request, 'chores/index.html', { 'chores': chores})

def chores_detail(request, chore_id):
  chore = Chore.objects.get(id=chore_id)
  return render(request, 'chores/detail.html', { 'chore': chore })


# Create your views here.
class ChoreCreate(CreateView):
  model = Chore
  fields = '__all__'
#   success_url = '/chores/{chore_id}'

class ChoreUpdate(UpdateView):
  model = Chore
    # disallow the changing of the name and type of the chore
    # only allow changing of description (what will get done) and
    # the amount (b/c its being negotiated)   
  fields = ['description', 'amount']

class ChoreDelete(DeleteView):
   model = Chore
   success_url = '/chores'

