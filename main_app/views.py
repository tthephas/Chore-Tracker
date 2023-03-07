from django.shortcuts import render

# Create your views here.


# Build the home view
def home(request):
  return render(request, 'home.html')

# About route/page
def about(request):
  return render(request, 'about.html')

