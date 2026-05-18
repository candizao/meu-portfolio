from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm


def is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()


# ── LISTA ─────────────────────────────────────────────────────────────────────

def artigos_lista(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/lista.html', {
        'artigos': artigos,
        'is_autor': is_autor(request.user),
    })


# ── DETALHE ───────────────────────────────────────────────────────────────────

def artigo_detalhe(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comentarios = artigo.comentarios.all()
    form_comentario = ComentarioForm()

    # sessão para likes anónimos
    if not request.session.session_key:
        request.session.create()
    sessao = request.session.session_key
    ja_deu_like = artigo.likes.filter(sessao=sessao).exists()

    return render(request, 'artigos/detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
        'ja_deu_like': ja_deu_like,
        'is_autor': is_autor(request.user),
    })


# ── CRIAR ─────────────────────────────────────────────────────────────────────

@login_required
def artigo_criar(request):
    if not is_autor(request.user):
        raise PermissionDenied
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos_lista')
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Novo Artigo'})


# ── EDITAR ────────────────────────────────────────────────────────────────────

@login_required
def artigo_editar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if not is_autor(request.user) or artigo.autor != request.user:
        raise PermissionDenied
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigo_detalhe', pk=artigo.pk)
    return render(request, 'artigos/form.html', {'form': form, 'titulo': f'Editar — {artigo.titulo}'})


# ── LIKE ──────────────────────────────────────────────────────────────────────

def artigo_like(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if not request.session.session_key:
        request.session.create()
    sessao = request.session.session_key
    like, criado = Like.objects.get_or_create(artigo=artigo, sessao=sessao)
    if not criado:
        like.delete()  # toggle: se já deu like, remove
    return redirect('artigo_detalhe', pk=pk)


# ── COMENTAR ──────────────────────────────────────────────────────────────────

@login_required
def artigo_comentar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
    return redirect('artigo_detalhe', pk=pk)