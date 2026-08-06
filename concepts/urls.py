from django.urls import path
from . import views

app_name = 'concepts'

urlpatterns = [
    path('', views.index, name='index'),
]