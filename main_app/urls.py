#this is the equivalent of a js 'require' statement
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # static routes
    path('' , views.home, name='home'),
    path('about/', views.about, name='about'),
    # Cat routes
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/new/', views.add_cat, name='add_cat'),
    path('cats/<int:cat_id>/delete/', views.delete_cat, name='delete_cat'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/<int:cat_id>/edit/', views.edit_cat, name='edit_cat'),
    # Cat feeding
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # Cat toys
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    #auth 
    path('accounts/signup', views.signup, name='signup')
]