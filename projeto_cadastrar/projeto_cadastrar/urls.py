from app_cadastrar import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
    #rota, view responsavel, identificador
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar, name='Adicionardados'),
    path('usuario/', views.usuarios, name='listagem_usuarios'),
    path('usuario/<int:id>/excluir/', views.excluir_usuario, name='excluir_usuario'),
    path('usuario/<int:id>/editar/', views.editar_usuario, name='editar_usuario'),
]
