"""
El direcrio templates no viene por defecto en Django así que hay que crearlo!

Creamos también un archivo __init__.py para que Python pueda localizarlo como módulo!

Por defecto la config TEMPLAES de django buscará un subdirectorio app\templates dentro de cada app para localizar las plantillas.

Aparentemente aun SE PUEDE colocar en app\templates\template.html, Django no será capaz de diferenciar entre:

app1\templates\index.html
app2\templates\index.html

Pero sí entre:

app1\templates\app1\index.html
app2\templates\app2\index.html

El motivo es que el espacio de búsqueda para el loader de templates empieza en \templates no en app\templates para TODAS las apps, asi que aunque parezca un coñazo dentro de \templates hay que volver a crear un directorio con el nombre de la app (o un nombre único cualquiera).
"""