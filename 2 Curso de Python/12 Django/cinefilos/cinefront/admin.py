from django.contrib import admin

# Register your models here.

from .models import Pelicula, Director

# Vista de director

class PeliculaInline(admin.StackedInline):
    model = Pelicula
    extra = 1

class DirectorAdmin(admin.ModelAdmin):
    inlines = [PeliculaInline]
    list_display = ('nombre', 'nacimiento')
    list_filter = ['nacimiento']
    search_fields = ['nombre']


# Los .register sólo toman 2 argumentos, y no podemos meter
# modelos en una sola línea
admin.site.register(Director, DirectorAdmin)
admin.site.register(Pelicula)


"""
# Vista de película

class DirectorInline(admin.StackedInline):
    model = Director
    extra = 2

class PeliculaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Para redactar', {'fields': ['nombre', 'resumen']}),
        ('Pinchar & Clicar', {'fields': ['duracion', 'lanzamiento','director']}),
    ]

    inlines = [DirectorInline]

admin.site.register(Pelicula, PeliculaAdmin)
"""