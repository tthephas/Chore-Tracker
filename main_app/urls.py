from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  
  path('parents/', views.parents_index, name='parents_index'),
  path('parents/<int:parent_id>/', views.parents_detail, name='parents_detail'),
  path('parents/create/', views.ParentCreate.as_view(), name='parents_create'),
  path('parents/<int:pk>/update', views.ParentUpdate.as_view(), name='parents_update'),
  path('parents/<int:pk>/delete', views.ParentDelete.as_view(), name='parents_delete'),

  path('parents/<int:parent_id>/add_kid/', views.add_kid, name='add_kid'),

  path('kids/<int:kid_id>/assoc_chore/<int:chore_id>/', views.assoc_chore, name='assoc_chore'),
  # add photo
  path('kids/<int:kid_id>/add_photo/', views.add_photo, name='add_photo'),
  #delete photo
  path('kids/<int:kid_id>/delete_photo/<int:pk>/', views.PhotoDelete.as_view(), name='delete_photo'),
  
  path('kids/', views.kids_index, name='kids_index'),
  path('kids/<int:kid_id>/', views.kids_detail, name='kids_detail'),
  path('kids/create/', views.KidCreate.as_view(), name='kids_create'),
  path('kids/<int:pk>/update', views.KidUpdate.as_view(), name='kids_update'),
  path('kids/<int:pk>/delete', views.KidDelete.as_view(), name='kids_delete'),
  
  
  path('chores/', views.chores_index, name='chores_index'),
  path('chores/create/', views.ChoreCreate.as_view(), name='chores_create'),
  path('chores/<int:chore_id>/', views.chores_detail, name='chores_detail'),
  path('chores/<int:pk>/update', views.ChoreUpdate.as_view(), name='chores_update'),
  path('chores/<int:pk>/delete', views.ChoreDelete.as_view(), name='chores_delete'),

  path('accounts/signup/', views.signup, name='signup'),
]

