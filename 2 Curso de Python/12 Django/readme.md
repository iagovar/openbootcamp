En este ejercicio tendrás que crear una aplicación en Django que almacene datos de directores de cine y luego se puedan ver sus películas, así como una descripción de las mismas.

Tienes que personalizar el admin de la aplicación y a su vez crear las vistas de cada una de las partes de la aplicación.

---

Proyecto sobre **Pipenv**.

## Algunas consideraciones sobre Django

Django usa un esquema similar a MVC, pero le llama Model View Template.

![Esquema Funcionamiento Django](esquema-django.png)

### Modelo

Igual que en el esquema MVC, el modelo define relacines entre los datos. En Django básicamente se traslada en la definición del schema de la BD escogida.

En principio al usar SQLite definir los modelos miApp/models.py y ejecutar los comandos sobre migraciones, el modelo se implanta automáicamente en la BD.

Presumo, porque no lo he probado, que sucederá lo mismo en DBs cliente-servidor, al otorgarle a Django un user con privilegios de admin.

### Vista

Las vistas en Django definen más bien la lógica que la presentación, el nombre es confuso. Son básicamente funciones que determinan el enrutamiento y transformación de los datos.

Para apuntar a las vistas es necesario definir en *urls.py* qué tipo de URLs apuntan a qué vistas.

### Template/Plantilla

Aquí es donde Django define cómo se muestran los datos. El esquema de plantillas se parece a Twig.


## Info adicional

- Introducción a Django [MDN](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Introduction)

- Understanding MVC pattern in Django [Medium Blog](https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django-edda05b9f43f)

- ¡18h long! [Django for Everybody](https://www.youtube.com/watch?v=o0XbHvKxw7Y)