from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Pedidos(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Orcamento(models.Model):
    produto = models.ManyToManyField(User)
    preco = models.DecimalField(decimal_places=2, max_digits=9)