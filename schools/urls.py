from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('Elearning/', views.Elearning, name='Elearning'),
    path('Seniorone/', views.Seniorone, name='Seniorone'),
    path('Seniortwo/', views.Seniortwo, name='Seniortwo'),
    path('Seniorthree/', views.Seniorthree, name='Seniorthree'),
    path('Seniorfour/', views.Seniorfour, name='Seniorfour'),
    path('Seniorfive/', views.Seniorfive, name='Seniorfive'),
    path('Seniorsix/', views.Seniorsix, name='Seniorsix'),
]

