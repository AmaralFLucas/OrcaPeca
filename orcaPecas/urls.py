from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('solicitar-orcamento/', views.solicitar_orcamento, name='solicitar-orcamento'),
]