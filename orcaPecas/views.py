from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required

def solicitar_orcamento(request):
    pass
    # if request.method == "POST":
    #     modelo = request.POST['modelo']
    #     preco = request.POST['preco']
    #     descricao = request.POST['descricao']
    #     quantidade = request.POST['quantidade']
    #     codigo = request.POST['codigo']
    #     em_estoque = False
    #     if int(quantidade) > 0:
    #         em_estoque = True
    #     data_criacao = datetime.now()
          itens_orcamento = request.POST['teste'].json()

    #     Produtos.objects.create(
    #         nome=nome,
    #         preço=preco,
    #         descricao=descricao,
    #         quantidade=quantidade,
    #         codigo=codigo,
    #         em_estoque=em_estoque,
    #         data_criacao=data_criacao
    #     )

    #     return redirect('index')
    
    # else:
    #     return render(request, 'pages/adicionar_produto.html')