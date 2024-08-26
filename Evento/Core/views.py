from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["GET"])
def HomeView(request):
    data = {
        "name": "Evento",
        "description": "A powerful event management platform",
        "version": "1.0.0",
        "features": [
            "Event creation",
            "Ticket management",
            "Attendee tracking",
            "Analytics dashboard"
        ]
    }
    return JsonResponse(data)
