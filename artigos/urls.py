from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_lista, name='artigos_lista'),
    path('<int:pk>/', views.artigo_detalhe, name='artigo_detalhe'),
    path('criar/', views.artigo_criar, name='artigo_criar'),
    path('<int:pk>/editar/', views.artigo_editar, name='artigo_editar'),
    path('<int:pk>/like/', views.artigo_like, name='artigo_like'),
    path('<int:pk>/comentar/', views.artigo_comentar, name='artigo_comentar'),
]