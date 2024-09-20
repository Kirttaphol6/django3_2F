from django.urls import path
from . import views

urlpatterns = [
    path('blogd/', views.blogd, name='blogd'),
]