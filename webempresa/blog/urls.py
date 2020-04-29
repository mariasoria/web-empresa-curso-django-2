from django.urls import path
from . import views

urlpatterns = [
    # Paths blog
    path('', views.blog, name='blog'),
    # creo el path dinamico para las categorias de forma que se accedera a cada categoria con la url:
    # "127.0.0.1:8000/blog/category/id_categoria"
    # <category_id> => es la forma dinamica de declararlo. Detecta todo lo que hay entre /<>/, 
    # lo toma como un parámetro y se lo pasa a la vista "blog/views.py", 
    # lo captura en "def category", el parametro que dice "category_id"
    # pero es un string y yo lo quiero en entero, asi que lo convierto antes de mandarlo a la vista
    path('category/<int:category_id>/', views.category, name='category'),
    path('<int:post_id>/', views.post, name='post')
]