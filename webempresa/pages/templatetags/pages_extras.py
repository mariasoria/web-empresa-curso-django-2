from django import template
from pages.models import Page

# Creo un template tag para poder enviarme las paginas de sample
# una vez hecho, tengo que registrarlo en la lib de templates
# 1 - importamos el modulo de registros de templates
# 2 - transformamos una funcion normal en un tag simple


# 1
register = template.Library()

# 2
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
    # Devuelve la lista de páginas