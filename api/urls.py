from django.urls import path

from api.views import PessoaListarCriarView, PessoaEditarBuscarDeletarView

urlpatterns = [
    path(
        'pessoa/',
        PessoaListarCriarView.as_view(),
        name='pessoa-listar-criar-view'
    ),
    path(
        'pessoa/<int:pk>',
        PessoaEditarBuscarDeletarView.as_view(),
        name='pessoa-editar-buscar-deletar-view'
    ),
]