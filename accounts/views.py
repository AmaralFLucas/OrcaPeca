from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):

    if request.method == "POST":
        usuario = request.POST['username']
        senha = request.POST['password']

        verificarUsuario = auth.authenticate(request, username = usuario, password = senha)
        print(verificarUsuario)

        if verificarUsuario != None:
            auth.login(request, verificarUsuario)
            return redirect('index')
        else:
            return redirect('login')

    else:
        return render(request, 'pages/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
