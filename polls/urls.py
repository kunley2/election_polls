from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lga/', views.lga, name='lga'),
    path('create', views.poll_unit, name='create')
]