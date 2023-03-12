from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chore, Kid, Parent, Photo
from django.views.generic.detail import DetailView
from .forms import KidForm

import uuid
import boto3
from django.conf import settings

AWS_ACCESS_KEY = settings.AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
S3_BUCKET = settings.S3_BUCKET
S3_BASE_URL = settings.S3_BASE_URL



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

  id_list = kid.chores.all().values_list('id')

  chores_kid_hasnt_done = Chore.objects.exclude(id__in=id_list)

  return render(request, 'kids/detail.html', { 'kid': kid, 'chores': chores_kid_hasnt_done })

def assoc_chore(request, kid_id, chore_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Kid.objects.get(id=kid_id).chores.add(chore_id)
  return redirect('kids_detail', kid_id=kid_id)


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
  fields = ['name', 'age','description', 'current_balance']
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


def add_photo(request, kid_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file: 
      s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      try:
        s3.upload_fileobj(photo_file, S3_BUCKET, key)
        url = f"{S3_BASE_URL}{S3_BUCKET}/{key}"
        photo = Photo(url=url, kid_id=kid_id)
        photo.save()
      except Exception as error:
        print('Error uploading photo', error)
        return redirect('kids_detail', kid_id=kid_id)
    return redirect('kids_detail', kid_id=kid_id)

