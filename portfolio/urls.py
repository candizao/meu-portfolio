from django.urls import path
from .views import (
    home, sobre,
    licenciatura_detail, uc_detail, projeto_detail, tfc_detail,
    projeto_criar, projeto_editar, projeto_apagar,
    tecnologia_criar, tecnologia_editar, tecnologia_apagar,
    competencia_criar, competencia_editar, competencia_apagar,
    formacao_criar, formacao_editar, formacao_apagar,
)

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),

    path('licenciatura/<int:pk>/', licenciatura_detail, name='licenciatura_detail'),
    path('uc/<int:pk>/', uc_detail, name='uc_detail'),
    path('projeto/<int:pk>/', projeto_detail, name='projeto_detail'),
    path('tfc/<int:pk>/', tfc_detail, name='tfc_detail'),

    path('projeto/criar/', projeto_criar, name='projeto_criar'),
    path('projeto/<int:pk>/editar/', projeto_editar, name='projeto_editar'),
    path('projeto/<int:pk>/apagar/', projeto_apagar, name='projeto_apagar'),

    path('tecnologia/criar/', tecnologia_criar, name='tecnologia_criar'),
    path('tecnologia/<int:pk>/editar/', tecnologia_editar, name='tecnologia_editar'),
    path('tecnologia/<int:pk>/apagar/', tecnologia_apagar, name='tecnologia_apagar'),

    path('competencia/criar/', competencia_criar, name='competencia_criar'),
    path('competencia/<int:pk>/editar/', competencia_editar, name='competencia_editar'),
    path('competencia/<int:pk>/apagar/', competencia_apagar, name='competencia_apagar'),

    path('formacao/criar/', formacao_criar, name='formacao_criar'),
    path('formacao/<int:pk>/editar/', formacao_editar, name='formacao_editar'),
    path('formacao/<int:pk>/apagar/', formacao_apagar, name='formacao_apagar'),
]