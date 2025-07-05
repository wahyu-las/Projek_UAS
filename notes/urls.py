# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/new/', views.note_create, name='note_create'),
    path('note/<int:pk>/edit/', views.note_update, name='note_update'),
]