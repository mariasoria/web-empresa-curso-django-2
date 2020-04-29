from django.urls import path
from . import views

urlpatterns = [
    # Paths blog
    path('', views.delegations, name='delegations')
]