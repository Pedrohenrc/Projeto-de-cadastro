from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.views.decorators.http import require_POST
from .forms import UsuarioForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def adicionar(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.numcard = request.POST.get('card_number')
        novo_usuario.titcard = request.POST.get('card_holder')
        novo_usuario.expiry_date = request.POST.get('expiry_date')
        novo_usuario.securycard = request.POST.get('cvv')
        novo_usuario.save()
        
        return render(request, 'home.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

@require_POST
def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)
    usuario.delete()
    return redirect('listagem_usuarios')

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    
    contexto = {
        'form': form,
        'usuario': usuario
    }
    return render(request, 'editar.html', contexto)