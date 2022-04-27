from django.shortcuts import render, HttpResponse
from carro.carro import Carro
from servicios.models import Servicio

# Create your views here.

def home(request):

    carro = Carro(request)

    return render(request, "ProyectoWebApp/home.html")
    

#def tienda(request):

 #   return render(request, "ProyectoWebApp/tienda.html")
    
#def blog(request):

#    return render(request, "ProyectoWebApp/blog.html")
    
#def contacto(request):

#    return render(request, "ProyectoWebApp/contacto.html")
    
