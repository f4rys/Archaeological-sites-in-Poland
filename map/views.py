from django.shortcuts import render
from django.http import JsonResponse
from map.models import Excavations

def index(request):
    return render(request, 'index.html')

def get_excavation_data(request, inspire_id):
    try:
        excavation = Excavations.objects.get(INSPIRE_ID=inspire_id)
        data = {
            'Funkcja': excavation.FUNKCJA.capitalize(),
            'Chronologia': excavation.CHRONOLOGIA.capitalize(),
            'Miejscowość': excavation.MIEJSCOWOSC.title(),
            'Link': excavation.LINK
        }
        return JsonResponse(data)
    except Excavations.DoesNotExist:
        return JsonResponse({'error': 'Excavation not found'}, status=404)