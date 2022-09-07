from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('operaciones', views.operaciones, name='operaciones'),
    path('respuesta_operaciones', views.respuesta_operaciones, name='respuesta_operaciones'),
    path('cilindro', views.cilindro, name='cilindro'),
    path('respuesta_cilindro', views.respuesta_cilindro, name='respuesta_cilindro'),
]