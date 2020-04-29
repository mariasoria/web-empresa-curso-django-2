from django.db import models

# Create your models here.
class Link (models.Model):
    # SlugField: obliga a usar caracteres alfanumericos, guiones o barras SOLO
    # perfecto para usarlo como clave a modo de registro, y al que se accede como un diccionario
    # unique = True, porque cada red social debe tener su clave unica
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name = "Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['-name']

    def __str__(self):
        # devuelve el nombre en el admin
        return self.name