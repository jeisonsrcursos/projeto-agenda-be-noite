from django.shortcuts import render
from rest_framework import generics, viewsets

from api.models import Pessoa
from api.serializers import PessoaSerializers

# API Versão 1
class PessoaListarCriarView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializers

class PessoaEditarBuscarDeletarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializers


# API Versão 2
class PessoaView(viewsets.ModelViewSet):
    # Já fornece: GET | POST | PUT | PATCH | DELETE
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializers

