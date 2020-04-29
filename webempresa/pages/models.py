from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name = "Título", max_length=200)
    content = RichTextField(verbose_name='Contenido')

    # indicara con un valor entero el orden en que mostrar cada pagina (0 para el primero en mostrarse)
    order = models.SmallIntegerField(verbose_name="Orden", default=0) 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['order', 'title']

    def __str__(self):
        # devuelve el nombre en el admin
        return self.title