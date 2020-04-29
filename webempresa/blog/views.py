from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
# recupera todos los posts
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})


# category_id: es el id unico en la BD de cada categoria
# Recupera la categoria a partir del ID que se le pasa en la url
# luego muestra solo los posts que corresponden a esa categoria
def category(request, category_id):
    # en vez de hacer objects.all, podemos hacer objects.get porque nos permite 
    # coger un unico registro filtrando por los campos especificados entre ()
    # category = Category.objects.get(id=category_id) # encontrara la categoria con el id que se le ha pasado
    # PERO vamos a usar el de bajo, xq queremos tratar la excepcion de si se introduce un numero de 
    # categoria que no exista, poder gestionar la excepcion
    category = get_object_or_404(Category, id=category_id)
    
    # Mostraremos los posts de esa categoria desde el html con:
    # category.post_set.all; con esto ya que puedes hacer un modelo (category), 
    # otro modelo relacionado con el(post) y con _set.all todas las instancias 
    # relacionadas del 2 modelo con el primero
    
    return render(request, "blog/category.html", {'category':category})
    # el diccionario de contexto {'category':category} 
    # es lo que les estoy pasando al template category.html
    # Por eso, luego desde el template puedo acceder a lo que haya ahí dentro

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post.html", {'post':post})