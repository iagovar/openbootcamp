from django.urls import path

from . import views

# Esto genera un namespace para todas as url patterns
# así evitamos que django se confunda si hay varias apps
# con views que se llaman igual
app_name = 'cinefront'

urlpatterns = [
    # ex: /pelis/
    path('', views.index, name='index'),
    # ex: /pelis/2
    path('<int:inputPagination>/', views.index, name='index'),
    # ex: /busqueda/
    path('busqueda/', views.busqueda, name='busqueda'),
    # ex: pelis/pelicula/3
    path('pelicula/<int:peliculaId>/', views.pelicula, name='pelicula'),
    # ex pelis/director/3
    path('director/<int:directorId>/', views.director, name='director')

]