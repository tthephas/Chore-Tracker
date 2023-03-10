from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chore, Kid, Parent
from django.views.generic.detail import DetailView
from .forms import KidForm



# Build some chores to start

# chores = [
#   {'name': 'Fold the Laundry', 'type': 'cleaning', 'description': 'Folded and put away my clothes today', 'amount': 5},
#   {'name': 'Load Dishwasher', 'type': 'cleaning', 'description': 'I put 4 plates and 2 cups in dishwasher after dinner', 'amount': 3},
# ]

# kids = [
#   {'name': 'Mya', 'age': 11, 'description': 'very silly'},
#   {'name': 'Ryan', 'age': 9, 'description': 'very funny'}
# ]

# parents = [
#   {'name': 'Josh', 'children': 2},
#   {'name': 'John', 'children': 3}
# ]


# Build the home view
def home(request):
  return render(request, 'home.html')

# About route/page
def about(request):
  return render(request, 'about.html')

# Add the parents index view
def parents_index(request):
  parents = Parent.objects.all()
  return render(request, 'parents/index.html', { 'parents': parents })

def parents_detail(request, parent_id):

  parent = Parent.objects.get(id=parent_id)
  kid_form = KidForm()
  return render(request, 'parents/detail.html', { 'parent': parent, 'kid_form': kid_form })

...

# add this new function below cats_detail
def add_kid(request, parent_id):
  form = KidForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_kid = form.save(commit=False)
    new_kid.parent_id = parent_id
    new_kid.save()
  return redirect('parents_detail', parent_id=parent_id)


# Add the kids index view
def kids_index(request):
  kids = Kid.objects.all()
  return render(request, 'kids/index.html', { 'kids': kids })

def kids_detail(request, kid_id):
  kid = Kid.objects.get(id=kid_id)
  return render(request, 'kids/detail.html', { 'kid': kid })

# Add the chores index view
def chores_index(request):
  chores = Chore.objects.all()
  return render(request, 'chores/index.html', { 'chores': chores})

def chores_detail(request, chore_id):
  chore = Chore.objects.get(id=chore_id)
  return render(request, 'chores/detail.html', { 'chore': chore })


## assoc chores to kids
## unlike feedings or toys that were on same page. how do we link them?
# def assoc_chore(request, kid_id, chore_id):
#   Kid.objects.get(id=kid_id).chores.add(chore_id)
#   return redirect('kids_detail', kid_id=kid_id)


# Create your views here.
# PARENT VIEWS
class ParentCreate(CreateView):
  model = Parent
  fields = '__all__'


class ParentUpdate(UpdateView):
  model = Parent
  
  fields = ['children']

class ParentDelete(DeleteView):
   model = Parent
   success_url = '/parents'


# Create your views here.
# KID VIEWS

class KidCreate(CreateView):
  model = Kid
  fields = ['name', 'age','description']
#   success_url = '/chores/{chore_id}'

class KidUpdate(UpdateView):
  model = Kid
  # can they change their parent? like from mom to dad. hmmm
  fields = ['age','description']

class KidDelete(DeleteView):
   model = Kid
   success_url = '/kids'


# Create your views here.
# CHORE VIEWS

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

