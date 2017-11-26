# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# from forms import NameForm

# Create your views here.
def home(request):
    data = {}

    if request.method == 'POST':
        data['community'] = request.POST.get('community', 'name not found')
        data['OID'] = request.POST.get('OID', 'name not found')
        data['endereco'] = request.POST.get('endereco', 'name not found')
        data['porta'] = request.POST.get('porta', 'name not found')

    # Pra debugar 
    # import pdb;pdb.set_trace()
    # Chamar funcao edson abaixo, tirar o comentário para chamar
    # item = snmp(data['community'],data['OID'],  data['endereco'] ,data['porta'])
    return render(request, 'core/index.html', data)


def informacoes(request):
        return render(request, 'core/informacoes.html')
