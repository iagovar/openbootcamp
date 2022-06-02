# Instalamos Django
pipenv install django

# Entramos en la shell de pipenv
pipenv shell

# Ejecutamos el comando de inicio con "." para que lo instale en el directorio desde el que ejecutamos el comando
# y no cree ./directorio/directorio-de-instalacion
django-admin startproject cinefilos .


# Ejecutamos el servidor de prueba
python3 manage.py runserver
firefox localhost:8000
