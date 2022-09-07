from django.shortcuts import render
import math


# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def operaciones(request):
    return render(request, 'encuesta/operaciones.html')

def respuesta_operaciones(request):
    expr = request.POST['num1'] + request.POST['operacion'] + request.POST['num2']
    result = eval(expr)
    context = {
        'titulo' : 'Respuesta de la operacion',
        'resultado' : result,
    }
    return render(request, 'encuesta/respuesta_operaciones.html', context)

def cilindro(request):
    return render(request, 'encuesta/cilindro.html')

def respuesta_cilindro(request):
    expr = request.POST['num2']+"*"+ "((" + request.POST['num1'] + "/2)**2)"
    result = float(eval(expr)) * math.radians(180)
    
    context = {
        'titulo' : 'Resultado:',
        'resultado' : result,
    }
    return render(request, 'encuesta/respuesta_cilindro.html', context)