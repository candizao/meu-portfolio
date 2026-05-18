from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Licenciatura, UnidadeCurricular, Projeto, TFC, Tecnologia, Formacao, Competencia, TipoTecnologia, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm


def is_gestor(user):
    return user.is_authenticated and user.groups.filter(name='gestor-portfolio').exists()


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
        'is_gestor': is_gestor(request.user),
    }
    return render(request, 'portfolio/home.html', context)


# ── SOBRE ─────────────────────────────────────────────────────────────────────

def sobre(request):
    tipos = TipoTecnologia.objects.prefetch_related('tecnologias').all()
    makingof = MakingOf.objects.all()
    context = {
        'tipos': tipos,
        'makingof': makingof,
    }
    return render(request, 'portfolio/sobre.html', context)


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
    context = {'uc': uc, 'projetos': uc.projetos.all()}
    return render(request, 'portfolio/uc_detail.html', context)


def projeto_detail(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'portfolio/projeto_detail.html', {'projeto': projeto})


def tfc_detail(request, pk):
    tfc = get_object_or_404(TFC, pk=pk)
    return render(request, 'portfolio/tfc_detail.html', {'tfc': tfc})


# ── CRUD PROJETO ──────────────────────────────────────────────────────────────

@login_required
def projeto_criar(request):
    if not is_gestor(request.user):
        raise PermissionDenied
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Criar Projeto', 'cancelar_url': 'home'})


@login_required
def projeto_editar(request, pk):
    if not is_gestor(request.user):
        raise PermissionDenied
    projeto = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': f'Editar — {projeto.titulo}', 'cancelar_url': 'home'})


@login_required
def projeto_apagar(request, pk):
    if not is_gestor(request.user):
        raise PermissionDenied
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('home')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': projeto.titulo, 'cancelar_url': 'home'})


# ── CRUD TECNOLOGIA ───────────────────────────────────────────────────────────

@login_required
def tecnologia_criar(request):
    if not is_gestor(request.user):
        raise PermissionDenied
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Adicionar Tecnologia', 'cancelar_url': 'home'})


@login_required
def tecnologia_editar(request, pk):
    if not is_gestor(request.user):
        raise PermissionDenied
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': f'Editar — {tecnologia.nome}', 'cancelar_url': 'home'})


@login_required
def tecnologia_apagar(request, pk):
    if not is_gestor(request.user):
        raise PermissionDenied
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('home')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': tecnologia.nome, 'cancelar_url': 'home'})


# ── CRUD COMPETÊNCIA ──────────────────────────────────────────────────────────

@login_required
def competencia_criar(request):
    if not is_gestor(request.user):
        raise PermissionDenied
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Adicionar Competência', 'cancelar_url': 'home'})


@login_required
def competencia_editar(request, pk):
    if not is_gestor(request.user):
        raise PermissionDenied
    competencia = get_object_or_404(Competencia, pk=pk)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': f'Editar — {competencia.nome}', 'cancelar_url': 'home'})


@login_required
def competencia_apagar(request, pk):
    if not is_gestor(request.user):
        raise PermissionDenied
    competencia = get_object_or_404(Competencia, pk=pk)
    if request.method == 'POST':
        competencia.delete()
        return redirect('home')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': competencia.nome, 'cancelar_url': 'home'})


# ── CRUD FORMAÇÃO ─────────────────────────────────────────────────────────────

@login_required
def formacao_criar(request):
    if not is_gestor(request.user):
        raise PermissionDenied
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Adicionar Formação', 'cancelar_url': 'home'})


@login_required
def formacao_editar(request, pk):
    if not is_gestor(request.user):
        raise PermissionDenied
    formacao = get_object_or_404(Formacao, pk=pk)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': f'Editar — {formacao.nome}', 'cancelar_url': 'home'})


@login_required
def formacao_apagar(request, pk):
    if not is_gestor(request.user):
        raise PermissionDenied
    formacao = get_object_or_404(Formacao, pk=pk)
    if request.method == 'POST':
        formacao.delete()
        return redirect('home')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': formacao.nome, 'cancelar_url': 'home'})