"""blogdehoryan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from App import views


urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('juegos',views.juegos, name= 'juegos'),
    path('integrantes',views.integrantes, name= 'integrantes'),
    path('donadores',views.donadores, name= 'donadores'),
    path('sugerencias',views.sugerencias, name= 'sugerencias'),
    #Patth formularios
    path('juegosFormulario',views.juegosformulario, name= 'juegosformulario'),
    path('integrantesFormulario',views.integrantesformulario, name= 'integrantesformulario'),
    path('donadoresFormulario',views.donadoresformulario, name= 'donadoresformulario'),
    path('sugerenciasFormulario',views.sugerenciasformulario, name= 'sugerenciasformulario'),
    #busqueda con form
    path('busquedaReview',views.busquedaReview, name= 'busquedaReview'),
    path('buscar/', views.buscar, name= 'buscar'),

]
