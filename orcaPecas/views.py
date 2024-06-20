import json
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Orcamento
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')

def index(request):
    if (request.user.is_staff):
        return render(request, 'pages/index2.html')
    elif (request.user.is_staff == False): 
        return render(request, 'pages/index.html')

def solicitar_orcamento(request):
    if request.method == "POST":
        criador = request.user.id
        nome = request.POST['cliente']
        modelo = request.POST['modelo']
        sinistro = request.POST['sinistro']
        oficina = request.POST['oficina']
        endereco = request.POST['endereco']
        placa = request.POST['placa']
        quantidade = request.POST['quantidade']
        peca = request.POST['itens']
        
        if peca:
            try:
                itens_orcamento = json.loads(peca)
            except json.JSONDecodeError:
                itens_orcamento = []
        else:
            itens_orcamento = []

        data_criacao = datetime.now()

        Orcamento.objects.create(
            criador_id=criador,
            nome=nome,
            modelo=modelo,
            comentarios_cliente=sinistro,
            oficina_entrega_nome=oficina,
            oficina_entrega_endereco=endereco,
            placa=placa,
            itens_orcamento=itens_orcamento,
            data_criacao=data_criacao
        )

        return redirect('index')
    
    else:
        return render(request, 'pages/solicitar_orcamento.html')
    
def exibir_orcamento(request):
    orcamentos = Orcamento.objects.filter(status='Pendente')
    return render(request, 'pages/orcamento_detalhes.html', {'orcamentos': orcamentos})

def orcamento(request, id):
    detalhes = Orcamento.objects.get(id=id)
    if request.method == "POST":
        resposta = request.POST['resposta']
        prazo = request.POST['prazo_entrega']
        valor = request.POST['valor_total']
        status = "aguardando_resposta_cliente"
        
        detalhes.comentarios_fornecedor = resposta
        detalhes.prazo_entrega = prazo
        detalhes.valor_total = valor
        detalhes.status = status
        detalhes.save()

        return exibir_orcamento(request)
    else:
        return render(request, 'pages/orcamento.html', {'detalhe': detalhes})
    
def orcados(request):
    orcamentos = Orcamento.objects.filter(status='aguardando_resposta_cliente')
    return render(request, 'pages/orcados.html', {'orcamentos': orcamentos})

def resposta_orcados(request, id):
    detalhes = Orcamento.objects.get(id=id)
    return render(request, 'pages/resposta_orcados.html', {'detalhe': detalhes})

def status_orcamento(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)
    
    if request.method == "POST":
        action = request.POST.get('action')
        
        if action == 'aprovar':
            orcamento.status = 'Aprovado'
        elif action == 'cancelar':
            orcamento.delete()
            return redirect('index')
        
        orcamento.save()
        return redirect('orcados')
    
    return render(request, 'pages/resposta_orcados.html', {'detalhe': orcamento})

def orcamentos_finalizados(request):
    orcamentos = Orcamento.objects.filter(status='Aprovado')
    return render(request, 'pages/finalizados.html', {'orcamentos': orcamentos})

def finalizados_info(request, id):
    detalhes = Orcamento.objects.get(id=id)
    return render(request, 'pages/finalizados2.html', {'detalhe': detalhes})