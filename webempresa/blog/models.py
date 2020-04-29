from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Modelo de usuario, contiene todos los usuarios registrados en nuestro panel de admin
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post (models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    
    # RELACIONA UN AUTOR CON UNO DE LOS USUARIOS REGISTRADOS, de forma que cada post tenga
    # siempre asignado UN SOLO autor (de entre los usuarios del sistema)
    # obligatorio pasarle on_delete, ya que si un usuario se borra, y tiene entradas asignadas...entonces que? 
    # Le indica a django lo que tiene que hacer si se borra el autor de una entrada ya publicada
    # si le ponemos on_delete=models.CASCADE, borrará todas las entradas (en cascada) que tenía este autor
    # sino, se quedarán las entradas sin autor
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    
    # RELACIONA EL POST (ENTRADA) CON LA CATEGORIA, PUDIENDO ESCOGER VARIAS CATEGORIAS PARA UN MISMO POST
    # relaciono también dos modelos, pero con la opcion de poder seleccionar varias categorias a una misma entrada
    # además le añado el related_name: que podré usar luego en el html para recuperar los posts dependiendo de la categoria
    # definiendo este related_name en una relacion, yo puedo ir a buscar la relacion inversamente a partir de ese campo
    # como si fuera otro campo más del modelo principal
    # el primer parámetro que se le pasa es el modelo con el que se creará la relacion:
    # en este caso, se creará una relacion Post <=> Categories (creándose también una tabla en la BD)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title
