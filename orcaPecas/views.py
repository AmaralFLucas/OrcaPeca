from django.shortcuts import render, redirect
from .models import Orcamento
from datetime import datetime
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'pages/index.html')

def solicitar_orcamento(request):
    if request.method == "POST":
        nome = request.POST['nome']
        modelo = request.POST['modelo']
        sinistro = request.POST['sinistro']
        oficina = request.POST['oficina']
        endereco = request.POST['endereco']
        placa = request.POST['placa']
        quantidade = request.POST['quantidade']
        # if int(quantidade) > 0:
        #     em_estoque = True
        data_criacao = datetime.now()
        itens_orcamento = request.POST['peca'].json()

        Orcamento.objects.create(
            nome=nome,
            moedlo=modelo,
            sinistro=sinistro,
            oficina=oficina,
            endereco=endereco,
            placa=placa,
            itens_orcamento=itens_orcamento,
            quantidade=quantidade,
            data_criacao=data_criacao
        )

        return redirect('index')
    
    else:
        return render(request, 'pages/solicitar_orcamento.html')