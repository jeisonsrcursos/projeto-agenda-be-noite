from django.urls import path
from rest_framework.routers import SimpleRouter

from api.views import PessoaListarCriarView, PessoaEditarBuscarDeletarView, PessoaView


# API V1
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

# API V2
router = SimpleRouter()
router.register(
    r'pessoa',
    PessoaView,
    basename='pessoa-listar-criar-buscar-deletar-view'
)