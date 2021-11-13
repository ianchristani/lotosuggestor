from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def loto(request):
    lista = []
    cont=0
    if request.method == 'POST':
        range_ = int(request.POST.get('range',False))
        amount = int(request.POST.get('amount',False))
        while cont <= amount:
            n = randint(1,range_+1)
            if n not in lista:
                lista.append(n)
                cont += 1
        resultado = lista
        return render(request,'loto.html',{'resultado':resultado})
    else:
        return render(request,'loto.html')