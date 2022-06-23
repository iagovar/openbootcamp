import datetime

from tkinter import CASCADE
from django.db import models
from django.utils import timezone
# Create your models here.

"""
En Django, cada clase representa una tabla en la BD. Las varaibles representan
las columnas de cada tabla, y los parámetros de los métodos field las características
que se transformarán en las sentencias SQL de iniciación de las tablas.

También parece que se puede incrustar algo de validación de datos pero no lo tengo
claro.

1. Edita tus modelos en este archivo
2. Corre manage.py makemigrations para crear el archivo que definirá la migración (se guardan en \migrations)
3. Corre manage.py migrate para aplicar los cambios definidos en makemigrations (se aplicará el último de \migrations)

    ¿Por qué comandos separados? VVV

    Porque así puedes guardar las migraciones en control de versiones, antes de aplicarlas directamente sobre la BD, pudiendo revisar lo que hiciste y facilitando la vida a otros devs.

"""

class Question(models.Model):
    # No es necesario especificar un unique ID porque Django ya lo hace
    # automáticamente
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        """
        La lógica de definir este método se puede leer aquí: https://stackoverflow.com/questions/45483417/what-is-doing-str-function-in-django

        Básicamente ya hay un método __str__ en modeLs.Model que sobreescribismo, porque
        el que viene por defecto simplemente lista el número de objetos..
        """
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """ 
    ForeignKey sirve para relacionar una tabla con otra. En este caso
    La tabla choice se relaciona con question.

    Hay que tener en cuenta que Django crea las tablas con un unique ID
    automáticamente, no es necesario especificarlo si no se quiere.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text