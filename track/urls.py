from django.urls import path
from . import views

app_name = 'track'

urlpatterns = [
    path('univ_list', views.univ_list, name='univ_list'),

]
