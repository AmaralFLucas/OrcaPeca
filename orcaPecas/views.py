from django.shortcuts import render, redirect
from .models import Orcamento
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    if (request.user.is_superuser):
        return render(request, 'pages/index.html')
    elif (request.user.is_staff):
        return render(request, 'pages/index2.html')

def solicitar_orcamento(request):
    if request.method == "POST":
        cliente = request.user.id
        # nome = request.POST['nome']
        modelo = request.POST['modelo']
        sinistro = request.POST['sinistro']
        oficina = request.POST['oficina']
        endereco = request.POST['endereco']
        placa = request.POST['placa']
        quantidade = request.POST['quantidade']
        peca = request.POST['peca']
        # if int(quantidade) > 0:
        #     em_estoque = True
        data_criacao = datetime.now()
        # itens_orcamento = request.POST['peca', 'quantidade'].json()

        Orcamento.objects.create(
            cliente_id=cliente,
            modelo=modelo,
            comentarios_cliente=sinistro,
            oficina_entrega_nome=oficina,
            oficina_entrega_endereco=endereco,
            # placa=placa,
            itens_orcamento={"peca":peca, "quantidade":quantidade},
            data_criacao=data_criacao
        )

        return redirect('index')
    
    else:
        return render(request, 'pages/solicitar_orcamento.html')
    
def pedidos_orcamentos(request):
    return render(request, 'pages/pedidos_orcamentos.html')