from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'conceitos', 'tecnologias', 'unidade_curricular', 'imagem', 'video_demo', 'github']


class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'logo', 'website', 'nivel_interesse', 'descricao']


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'descricao', 'projetos', 'tecnologias', 'formacoes']


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['nome', 'instituicao', 'ano', 'descricao']