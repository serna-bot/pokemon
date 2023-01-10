from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Pokemon

# Create your views here.
def home_page(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def pokemon_detail_view(request, pokemon_id, *args, **kwargs):
    data = {
        "poke_id": pokemon_id,
    }
    status = 200
    try:
        obj = Pokemon.objects.get(poke_id=pokemon_id)
        data['name'] = obj.name
    except:
        data['Message'] = "Error: Pokemon not found."
        status = 404
    
    return JsonResponse(data, status = status)