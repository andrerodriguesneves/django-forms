from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.validation import *


class PassagenForms(forms.Form):

    # Choices
    FLIGHT_CLASS = (
        (1, 'Economica'),
        (2, 'Executiva'),
        (3, 'Primeira Classe')
    )

    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data Pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do Vôo', choices=FLIGHT_CLASS)
    email = forms.EmailField(label='Email', max_length=200)
    informacoes = forms.CharField(label='Informações Adicionais', max_length=400, widget=forms.Textarea, required=False)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem = lista_de_erros[erro]
                self.add_error(erro, mensagem)

        return self.cleaned_data