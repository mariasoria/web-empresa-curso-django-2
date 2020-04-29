# definimos una funcion (cualquier nombre) con el parametro request
# Recuperamos lo que queremos poner como contexto global
# y lo devolvemos
from .models import Link

def context_dict(request):
    context = {}
    links = Link.objects.all()
    # generamos un diccionario con sus claves y las url
    for link in links:
        context[link.key] = link.url
        # ejemplo: 
        # context = {'LINK_TWITTER': 'www.twitter.com', 'LINK_FACEBOOK':...}
    return context
    # la idea es que este diccionario, extienda al contexto global
    # de manera que podamos utilizar las claves como una varibale en cualquier template
    # tenemos que añadirla a settings.py, 
    # en TEMPLATES en 'context_processors'