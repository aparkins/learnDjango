from django.shortcuts import render
from django.http import JsonResponse
from .models import Card, Location, Role
import random

def random_card(request):
    players = int(request.GET.get('players', '1'))
    location = request.GET.get('location', '')
    if (random.randint(1, players) > 1):
        cards = Card.objects.filter(location__description=location)
        card = cards[random.randint(0, len(cards)-1)]
        return JsonResponse({
            'location': card.location.description,
            'role': card.role.description})
    return JsonResponse({'role':'spy'})
