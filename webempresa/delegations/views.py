from django.shortcuts import render
from .models import Delegations

# Create your views here.
def delegations (request):
    delegations = Delegations.objects.all()
    return render(request, 'delegations/delegations.html', {'delegations': delegations})
