from django.db import models

# Create your models here.
class Delegations(models.Model):
    place = models.CharField(max_length= 100, verbose_name='Lugar', blank=False)
    name = models.CharField(max_length= 100, verbose_name='Persona encargada', blank=False)
    phone = models.CharField (max_length= 100, blank=True, null=True)
    email = models.EmailField(verbose_name='Email')
    main = models.BooleanField(verbose_name='Oficina principal', default=False)

    class Meta:
        verbose_name = 'Delegacion'
        verbose_name_plural = 'Delegaciones'
        ordering = ['-main', 'place']

    def __str__(self):
        return self.place
