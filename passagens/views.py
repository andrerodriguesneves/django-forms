from django.shortcuts import render
from passagens.forms import PassagenForms


# Create your views here.
def index(request):
    form = PassagenForms()
    contexto = {
        'form': form,
        'titulo': 'Seu melhor buscador de passagens aereas! '
    }
    return render(request, 'index.html', contexto)


def checkout(request):
    if request.method == 'POST':
        form = PassagenForms(request.POST)
        if form.is_valid():
            contexto = {
                'form': form,
                'titulo': 'CheckOut - Busca Passagens'
            }
            return render(request, 'checkout.html', contexto)
        else:
            contexto = {
                'form': form,
                'titulo': 'Seu melhor buscador de passagens aereas!'
            }
            return render(request, 'index.html', contexto)


