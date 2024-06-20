from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index, name='index2'),
    path('solicitar-orcamento/', views.solicitar_orcamento, name='solicitar-orcamento'),
    path('orcamento_detalhes/', views.exibir_orcamento, name='orcamento_detalhes'),
    path('orcamento/<int:id>', views.orcamento, name='orcamento'),
    path('orcados/', views.orcados, name='orcados'),
    path('resposta_orcados/<int:id>', views.resposta_orcados, name='resposta_orcados'),
    path('orcamento/status/<int:id>/', views.status_orcamento, name='status_orcamento'),
    path('finalizados/', views.orcamentos_finalizados, name='finalizados'),
    path('finalizados2/<int:id>', views.finalizados_info, name='finalizados2'),
]