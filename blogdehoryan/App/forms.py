from django import forms


#Creamos las clase formulario para cada uno de nuestros objetos:

class JuegoFormulario(forms.Form):
    #especificamos los campos del formulario
    nombre = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
    calificacion = forms.IntegerField()
    resena = forms.CharField(max_length=500)

class IntegranteFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    cargo = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)

class DonadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    nickname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)

class SugerenciaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
