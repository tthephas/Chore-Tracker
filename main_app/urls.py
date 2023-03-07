from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chores/', views.chores_index, name='index'),
  path('chores/<int:chore_id>/', views.chores_detail, name='detail'),
  path('chores/create/', views.ChoreCreate.as_view(), name='chores_create'),
]

