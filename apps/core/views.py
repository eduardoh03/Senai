from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import Configuracao


def home(request):
    configuracao = Configuracao.objects.all()

    # Esta verificação é apenas para não deixar o site em branco
    if len(configuracao) > 0:
        configuracao = configuracao[0]
    else:
        configuracao = {
            "slogan": "Slogan",
            "nome_empresa": "Nome da Empresa",
            "telefone": "(00) 00000-0000",
            "email": "email@amil.com"
        }

    dados = {
        "configuracao": configuracao,
    }
    return render(request, "home.html", dados)


def create_user(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        return redirect('entrar')
    return render(request, "create_user.html", {'form': form})


def entrar(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pagina_home')
        else:
            form.add_error(None, 'Nome de usuário ou senha incorretos')
    return render(request, "login.html", {'form': form})


@login_required(login_url='core/entrar')
def sair(request):
    logout(request)
    return redirect('pagina_home')
