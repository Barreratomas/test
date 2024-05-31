from django.shortcuts import render

def presentacion(request):
    return render(request, 'presentacion.html',{})



def fotos(request):
    return render(request, 'fotos.html',{})