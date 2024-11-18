from rest_framework import serializers

from api.models import Pessoa, Contato


class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = (
            'id',
            'nome',
            'endereco',
            'bairro',
            'cidade',
            'uf'
        )

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = (
            'id',
            'pessoa',
            'contato',
            'tipo',
            'descricao',
        )