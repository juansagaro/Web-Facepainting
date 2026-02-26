"""
URLs de la app webapp.

Cada ruta apunta a una vista que renderiza un template.
Los nombres (name=) permiten usar {% url 'home' %} en los templates
en vez de escribir URLs a mano — si un día cambias la URL, no tienes
que tocar ningún template.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('galeria/', views.galeria, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
    path('facepainting/', views.facepainting, name='facepainting'),
    path('bodypaint/', views.bodypaint, name='bodypaint'),
    path('glitterbar/', views.glitterbar, name='glitterbar'),
    path('talleres/', views.talleres, name='talleres'),
]
