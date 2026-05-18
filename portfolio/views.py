from django.shortcuts import render, get_object_or_404, redirect
from .models import Licenciatura, UnidadeCurricular, Projeto, TFC, Tecnologia, Formacao, Competencia
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm


# ── HOME ──────────────────────────────────────────────────────────────────────

def home(request):
    context = {
        'licenciaturas': Licenciatura.objects.all(),
        'ucs': UnidadeCurricular.objects.all(),
        'projetos': Projeto.objects.all(),
        'tfcs': TFC.objects.all(),
        'tecnologias': Tecnologia.objects.all(),
        'formacoes': Formacao.objects.all(),
        'competencias': Competencia.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)


# ── DETALHES ──────────────────────────────────────────────────────────────────

def licenciatura_detail(request, pk):
    licenciatura = get_object_or_404(Licenciatura, pk=pk)
    context = {
        'licenciatura': licenciatura,
        'ucs': licenciatura.ucs.all(),
        'tfcs': licenciatura.tfcs.all(),
    }
    return render(request, 'portfolio/licenciatura_detail.html', context)


def uc_detail(request, pk):
    uc = get_object_or_404(UnidadeCurricular, pk=pk)
    context = {
        'uc': uc,
        'projetos': uc.projetos.all(),
    }
    return render(request, 'portfolio/uc_detail.html', context)


def projeto_detail(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'portfolio/projeto_detail.html', {'projeto': projeto})


def tfc_detail(request, pk):
    tfc = get_object_or_404(TFC, pk=pk)
    return render(request, 'portfolio/tfc_detail.html', {'tfc': tfc})


# ── CRUD PROJETO ──────────────────────────────────────────────────────────────

def projeto_criar(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': 'Criar Projeto',
        'cancelar_url': 'home',
    })


def projeto_editar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': f'Editar Projeto — {projeto.titulo}',
        'cancelar_url': 'home',
    })


def projeto_apagar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('home')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': projeto.titulo,
        'cancelar_url': 'home',
    })


# ── CRUD TECNOLOGIA ───────────────────────────────────────────────────────────

def tecnologia_criar(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': 'Adicionar Tecnologia',
        'cancelar_url': 'home',
    })


def tecnologia_editar(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': f'Editar Tecnologia — {tecnologia.nome}',
        'cancelar_url': 'home',
    })


def tecnologia_apagar(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('home')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': tecnologia.nome,
        'cancelar_url': 'home',
    })


# ── CRUD COMPETÊNCIA ──────────────────────────────────────────────────────────

def competencia_criar(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': 'Adicionar Competência',
        'cancelar_url': 'home',
    })


def competencia_editar(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': f'Editar Competência — {competencia.nome}',
        'cancelar_url': 'home',
    })


def competencia_apagar(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    if request.method == 'POST':
        competencia.delete()
        return redirect('home')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': competencia.nome,
        'cancelar_url': 'home',
    })


# ── CRUD FORMAÇÃO ─────────────────────────────────────────────────────────────

def formacao_criar(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': 'Adicionar Formação',
        'cancelar_url': 'home',
    })


def formacao_editar(request, pk):
    formacao = get_object_or_404(Formacao, pk=pk)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {
        'form': form,
        'titulo': f'Editar Formação — {formacao.nome}',
        'cancelar_url': 'home',
    })


def formacao_apagar(request, pk):
    formacao = get_object_or_404(Formacao, pk=pk)
    if request.method == 'POST':
        formacao.delete()
        return redirect('home')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': formacao.nome,
        'cancelar_url': 'home',
    })