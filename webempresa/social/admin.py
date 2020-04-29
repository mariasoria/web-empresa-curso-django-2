from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # NOS HEMOS DADO CUENTA DE QUE DESDE EL PANEL ADMIN NO SE LE PUEDE ESPECIFICAR A UN GRUPO/USUARIO 
    # ESPECÍFICO QUE LOS VALORES DEL LINK DE LAS REDES SOCIALES SEAN DE SOLO LECTURA EN CASO DE NO SER ADMIN 
    # Así que tendremos que comprobarlos en tiempo de ejecucion. Para eso:
    # Debemos declarar la funcion: get_readonly_fields
    # # debe tener los atributos: self, request, obj=None
    # sobreescribirá la informacion de los readonly_fields despues de detectar
    # si el usuario que está accediendo tiene permisos o no, dependiendo del grupo
    # al que pertenezca. En este caso el grupo "personal"
    def get_readonly_fields(self, request, obj=None):
        # con request podremos comprobar, en tiempo de ejecucion, si hay un usuario identificado
        # y si ese usuario forma parte del grupo personal (que he creado yo a través del navegador)
        if(request.user.groups.filter(name="Personal").exists()): # comprobará si dentro del grupo personal existe ese usuario
            # devolveremos los valores que pasarán a ser solo lectura para este usuario
            # return('created', 'updated', 'key', 'name')
            # si por ejemplo no quiero ni que el usuario vea created y updated, pues no los devuelvo y ya está:
            return('key','name')
        else:
            # sino, pues solo serán de solo lectura los valores de created y updated
            return('created', 'updated')



    
admin.site.register(Link, LinkAdmin)
