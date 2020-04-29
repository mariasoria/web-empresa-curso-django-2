from django.urls import path
from . import views

urlpatterns = [
    # Paths pages
    # en la url irá:
    # el id de la pagina
    # un elemento de tipo slug (que sera el nombre de la pagina separado por guiones)
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]