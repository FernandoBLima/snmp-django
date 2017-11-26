from django import forms 
# from core.models import Post

class NameForm(forms.Form):
    community = forms.CharField(label='Digite a community desejada (default = public):', max_length=100),
    OID = forms.CharField(label='Digite o OID desejado:', max_length=100),
    endereco = forms.CharField(label='Digite o endereco do alvo:', max_length=100),
    porta = forms.CharField(label='Digite a porta do alvo (161 ou 9002):', max_length=100),