from django.shortcuts import render
from django.http import HttpResponse
from base.forms import CadastroForm
from base.models import Cadastro


# Create your views here.
def inicio(request):                        #tela de visualização (inicio)
    return render(request, 'inicio.html')
       
    return HttpResponse('Olá mundo')
    

def cadastro(request):                      #tela de visualização (cadastro)
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
            'form': form,
            'sucesso' : sucesso
        }        
    return render(request, 'cadastro.html', contexto)