from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime


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
    informacoes = forms.CharField(label='Informções Adicionais', max_length=400, widget=forms.Textarea, required=False)
