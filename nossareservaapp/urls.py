from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    UsuarioAPIView,
    AreaComumAPIView,
    AreaLocacaoAPIView,
    UsuariosAPIView,
    AreasComunsAPIView,
    AreaLocacoesAPIView,
    CondominioAPIView,
    CondominiosAPIView,
    UsuarioViewSet,
    AreaComumViewSet,
    AreaLocacaoViewSet,
    CondominioViewSet)

router = SimpleRouter()
router.register('usuarios', UsuarioViewSet)
router.register('areascomuns', AreaComumViewSet)
router.register('arealocacoes', AreaLocacaoViewSet)
router.register('condominio', CondominioViewSet)



urlpatterns = [
    path('usuarios/', UsuariosAPIView.as_view(), name='usuarios'),
    path('areascomuns/', AreasComunsAPIView.as_view(), name='areacomum'),
    path('locacoes/', AreaLocacoesAPIView.as_view(), name='locacoes'),
    path('usuarios/<int:pk>/', UsuarioAPIView.as_view(), name='usuarios'),

    path('usuarios/<int:usuario_pk>/locacoes', AreaLocacoesAPIView.as_view(), name='usuario-locacoes'),
    path('usuarios/<int:usuario_pk>/locacoes/<int:locacoes_pk>', AreaLocacaoAPIView.as_view(), name='usuario-locacao'),

    path('areascomuns/<int:pk>/', AreaComumAPIView.as_view(), name='areacomum'),
    path('locacoes/<int:locacoes_pk>/', AreaLocacaoAPIView.as_view(), name='locacoes'),
    path('condominio/<int:pk>/', CondominioAPIView.as_view(), name='condominio'),
    path('condominio', CondominiosAPIView.as_view(), name='locacoes'),
]