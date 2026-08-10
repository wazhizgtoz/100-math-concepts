from django.urls import path
from . import views

app_name = 'concepts'

urlpatterns = [
    path('', views.index, name='index'),
    path('conceito/<slug:slug>/', views.detalhe, name='detalhe'),
    path('toggle/<int:conceito_id>/', views.toggle_concluido, name='toggle_concluido'),
]