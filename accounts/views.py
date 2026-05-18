from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings
from django.urls import reverse
from .forms import RegistoForm

# Armazena tokens de magic link temporariamente (em memória)
magic_link_tokens = {}


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username ou password incorretos.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def registo_view(request):
    form = RegistoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            # Adiciona automaticamente ao grupo 'autores'
            grupo_autores, _ = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo_autores)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Erro no registo. Verifica os campos.')

    return render(request, 'accounts/registo.html', {'form': form})


def magic_link_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = get_random_string(32)
            magic_link_tokens[token] = user.pk
            link = request.build_absolute_uri(reverse('magic_link_verify', args=[token]))
            send_mail(
                subject='O teu link de acesso',
                message=f'Clica aqui para entrares no portfólio:\n\n{link}\n\nEste link é de uso único.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )
            messages.success(request, 'Link enviado para o teu email!')
        except User.DoesNotExist:
            messages.error(request, 'Não existe nenhuma conta com esse email.')

    return redirect('login')


def magic_link_verify(request, token):
    user_pk = magic_link_tokens.pop(token, None)
    if user_pk:
        try:
            user = User.objects.get(pk=user_pk)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('home')
        except User.DoesNotExist:
            pass
    messages.error(request, 'Link inválido ou expirado.')
    return redirect('login')