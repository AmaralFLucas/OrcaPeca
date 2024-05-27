from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index2'),
    path('solicitar-orcamento/', views.solicitar_orcamento, name='solicitar-orcamento'),
    path('pedidos-orcamentos/', views.pedidos_orcamentos, name='pedidos-orcamentos'),
]