from rest_framework import serializers

from api.models import Pessoa, Contato


class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = (
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
            'pessoa',
            'contato',
            'tipo',
            'descricao',
        )