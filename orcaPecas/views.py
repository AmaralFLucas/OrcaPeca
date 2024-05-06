from django.shortcuts import render
from django.contrib.auth.models import User

def requisitar_orcamento(request, id):
    orcamento = User.objects.get(id=request.user.id)