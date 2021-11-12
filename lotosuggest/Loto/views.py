from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.


def loto(request):
    lista = []
    cont=0
    if request.method == 'POST':
        opcao = request.POST.get('Loto',False)
        if opcao == "Loto":
            while cont <= 5:
                n = randint(1,61)
                if n not in lista:
                    lista.append(n)
                    cont += 1
            resultado = lista
        else:
            while cont < 15:
                n = randint(1,26)
                if n not in lista:
                    lista.append(n)
                    cont += 1
            resultado = lista

        return render(request,'loto.html',{'resultado':resultado})
    else:
        return render(request,'loto.html')