# Entrega1HoracioSanMartin
Entrega intermedia proyecto final CoderHouse por Horacio

# Indice:
1. Descripción de la página y botones
2. Desarrollo paso a paso del proyecto


# 1 Pagina el Blog de Horyan
Pagina que consiste en entregar reviews de videojuegos, formada por 4 modelos, los cuales son Juegos (juegos analizados), integrantes (equipo detrás, ya sean periodistas, informáticos, etc.), donadores (personas que se pueden inscribir para financiar el proyecto), sugerencias (sugerencias de nuevos juegos a analizar en el futuro).


Todo está configurado desde la App, de forma de que si se busca acceder al contenido se debe poner: 127.0.0.1:800/App/x, para acceder a las distintas ventanas, donde x puede ser: juegos, integrantes, donadores y sugerencias, que corresponden a las paginas de cada una de esas categorias en cuestión. 
###### (Actualizado: se agregó path de inicio para que no se vea feo)

Además, se agregaron los links formularios para ingresar nuevos datos que son de la forma App/XFormulario, con X tal como dijimos igual a juegos, integrantes, donadores y sugerencias. 

La pagina está hecha para que al momento de llenar un formulario correctamente te rediriga al inicio, y además, se agregaron en las paginas de cada uno de las categorias un botón con el link al formulario correspondiente por si se quieren agregar datos nuevos.

La única página que cambia es la de juegos, que tiene dos botones extras: agregar review, o buscar los juegos analizados de diferentes categorias de videojuegos: por el momento he ido agregando: simulacion, plataforma, RPG.

Por otra parte, se pueden ingresar datos directamente utilizando los links de Formularios.

Por lo tanto tenemos:

### Paginas principales
http://127.0.0.1:8000/App/ -> pagina de inicio
http://127.0.0.1:8000/App/juegos -> pagina de juegos
http://127.0.0.1:8000/App/integrantes -> pagina de integrantes
http://127.0.0.1:8000/App/donadores -> pagina de donadores
http://127.0.0.1:8000/App/sugerencias ->pagina de sugerencias de nuevos juegos a revisar

### Paginas de formularios
http://127.0.0.1:8000/App/juegosFormulario -> pagina de juegos
http://127.0.0.1:8000/App/integrantesFormulario -> pagina de integrantes
http://127.0.0.1:8000/App/donadoresFormulario -> pagina de donadores
http://127.0.0.1:8000/App/sugerenciasFormulario ->pagina de sugerencias de nuevos juegos a revisar


### Pagina buscar reviews por categoria
http://127.0.0.1:8000/App/busquedaReview  -> pagina para buscar redirige a pagina de resultados


# Notas de trabajo:

Indicación paso a paso de lo que se realizó (también disponible en notas.txt)

### 1. CREACION REPOSITORIO, MVT y APP ____________________________________________________________________________________________
- Uniendo a repositorio de github

- unimos al repositorio online
git clone https://github.com/horysan93/Entrega1SanMartin.git
cd Entrega1SanMartin

- Empezamos el Proyecto blogdehoryan

django-admin startproject blogdehoryan

- Creamos la app 
python manage.py startapp App

### 2. CREACION MODELOS ___________________________________________________________________________________________

- Vamos a crear un proyecto que tenga:

    - juegos (nombre, categoria, calificacion, reseña): reseñas de videojuegos analizados
    - integrantes (nombre, apellido, email, cargo): equipo del blog, periodistas, informaticos, etc.
    - donadores (nombre, nickname, email): listado de personas que aportaron a la pagina
    - sugerencias (nombre, categoria): listado de juegos que piden analizar

- Creamos los modelos en App/models.py: juegos, equipo, donadores, sugerencias
- agregamos la App en settings.py

- revisamos esté bien la app
python manage.py check App 

- Ahora haremos la estructura de sql:
python manage.py makemigrations
python manage.py sqlmigrate AppCoder 0001

python manage.py migrate

### 3. CREAMOS VIEWS ____________________________________________________________________________________________
- Creamos los views de cada uno de los modelos + pagina de inicio 
- agregamos App en settings, creamos urls.py en App y linkeamos las otras urls a las de la App

### 4. INSTALAMOS TEMPLATES y HERENCIAS __________________________________________________________________________
- Bajamos la template que utilizaremos
- En App creamos carpeta static y dentro carpeta App, pegamos los archivos descargados de la plantilla
- copiamos index en inicio.html y agregamos: {% load static %}
- editamos la plantilla que tenemos para que vaya tomando una forma más simple y trabajar en ella
- agregamos botones de cada pagina (el formato es el mismo de la clase aunqune cambia un poco el còdigo debido a la plantilla)

- Creamos template padre! 
- creamos block titulo y contenidoQueCambia para personalizar cada pagina (marcados con notas en padre.html)

### 5. PANEL DE ADMINISTRACION ____________________________________________________________________________________

- Entramos admin.py dentro de la App
- Creamos el usuario:
python manage.py createsuperuser
username: hory
mail: hory.san93@gmail.com
pass: qwerty123 

- Agregamos en admin.py los modelos para poder verlos desde el panel de administración, e importamos los modelos de models.py 

### 6. INGRESAR DATOS POR FORMULARIO _______________________________________________________________________________
- Creamos los formularios
- dentro de la App creamos forms.py 
    - agregamos la clase formulario para cada cosa 
    - creamos los html claseFormulario.html

- creamos en views variableFormulario
- agregamos los paths en urls.py 
- agregamos los formularios a cada templateFormulario.html 

NOTA: el programa no me estuvo funcionando por que había cambiado los modelos, entonces tuve que:
python manage.py makemigrations
python manage.py migrate 


### 7. BUSQUEDA DATOS CON FORMULARIO __________________________________________________________________________________

- Creamos en views buscar y busquedareviews
- creamos template de busquedareviews -> para ingresar la busqueda por categoria de juego analizados
- creamos template resultadosbusqueda -> entrega listado de juegos analizados que cumplen el criterio


### 8. UNIENDO VENTANAS PARA MÁS PLACER __________________________________________________________________________________
- la idea es que ahora cuando la gente entre a la página de juegos pueda dar click para que se redirija a las busquedas o ingrese DATOS
- mientras que para integrantes, donadores y sugerencias haya un link a los formularios (ya que aún no agregamos busquedas)
- agregados a la plantilla de juegos.html, de forma de que al momento de entrar se pueda hacer lo que sea.

#nota: pendiente aprender más html para enchular los botones

### 9. SUBIMOS A GITHUB ____________________________________________________________________________________________
git add .
git commit -m "Entrega intermedia"
git push origin main 

### 10. EXTRA _____________
agregamos un path de inicio y la view correspondiente para que si entran directamente a la pagina no se vea feo
