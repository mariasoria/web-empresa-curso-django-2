from django.shortcuts import render, get_object_or_404
from .models import Page

# page_id: es el id unico en la BD de cada categoria
# page_slug: es un paramentro de adorno que contiene el titulo separado por guiones
# Recupera la pagina a partir del ID que se le pasa en la url
# luego muestra la pagina correspondiente con el ID
def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)  
    return render(request, "pages/sample.html", {'page':page})
