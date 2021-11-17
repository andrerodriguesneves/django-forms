from django.shortcuts import render
from passagens.forms import PassagenForms, PessoaForms


# Create your views here.
def index(request):
    form = PassagenForms()
    pessoa_form = PessoaForms()
    contexto = {
        'form': form,
        'pessoa_form': pessoa_form,
        'titulo': 'Seu melhor buscador de passagens aereas! '
    }
    return render(request, 'index.html', contexto)


def checkout(request):
    if request.method == 'POST':
        form = PassagenForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {
                'form': form,
                'pessoa_form': pessoa_form,
                'titulo': 'CheckOut - Busca Passagens'
            }
            return render(request, 'checkout.html', contexto)
        else:
            contexto = {
                'form': form,
                'pessoa_form': pessoa_form,
                'titulo': 'Seu melhor buscador de passagens aereas!'
            }
            return render(request, 'index.html', contexto)


