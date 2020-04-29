from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    # podemos indicar las columnas que queremos mostrar en el admin
    list_display = ('title', 'author', 'published', 'post_categories') # aqui por ejemplo no se podría mostrar categories__name tal cual, 
    # porque pueden ser muchos elementos. 
    # Solucion: crear nuestros propios campos con el metodo (por ej) post_categories de más abajo
    
    # ordenar campos primero por un campo, y luego por un subcampo
    # si queremos ordenar solo por un campo, hay que terminar antes del ) con una coma. 
    # Ej. ordering = ('author',) # asi reconoce que es una tupla
    ordering = ('author', 'published')
    # mistrar un form de busqueda a partir de los campos que yo quiera
    # para buscar por author, como hace referencia a modelos relacionaddos
    # por eso hay que poner: author_username (que es el campo que tiene el modelo de usuario en la BD)
    # lo mismo para las categorias: categories__name
    search_fields = ('title','content', 'author__username', 'categories__name')
    # Los campos que tienen DateTimeField se pueden ordenar/buscar/filtrar con:
    date_hierarchy = 'published'
    # le podemos pasar campos para que los filtre. Normalmente son para campos relacionales
    # xq son campos que se repiten. Los titulos por ejemplo son únicos, no tiene sentido filtrarlos
    list_filter = ('author__username','categories__name')

    # obj: hace referencia a lo que se muestra en cada fila de cada elemento
    def post_categories (self, obj):
        # para que nos separe con comas las categorias que hay en cada obj que va recorriendo y las ordene por nombre
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    # puedo renombrar el nombre de la columna de estas categorias que voy a mostrar
    post_categories.short_description = 'Categorias'
    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
