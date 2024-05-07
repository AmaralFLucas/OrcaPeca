from django.db import models
from django.contrib.auth.models import User

# class Peca(models.Model):
#     nome = models.CharField(max_length=100)
#     quantidade = models.PositiveIntegerField()

class Orcamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    oficina_entrega_nome = models.CharField(max_length=100)
    oficina_entrega_endereco = models.TextField()
    status = models.CharField(max_length=20, default='Pendente')
    comentarios_cliente = models.TextField(blank=True, null=True)
    comentarios_fornecedor = models.TextField(blank=True, null=True)
    prazo_entrega = models.DateField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itens_orcamento = models.JSONField(default=list)
    
# class Pedidos(models.Model):
#     cliente = models.ForeignKey(User, on_delete=models.CASCADE)
#     nome = models.ForeignKey(Produto, on_delete=models.CASCADE)

# class Orcamento(models.Model):
#     produto = models.ManyToManyField(User)
#     preco = models.DecimalField(decimal_places=2, max_digits=9)