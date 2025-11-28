from django.shortcuts import render
from django.shortcuts import render

def saludo(request):
    return render(request, "saludo.html")

# Create your views here.
