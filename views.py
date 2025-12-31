from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Trip
import json


def home(request):
    return JsonResponse({"message": "Travel Buddy Finder API is working"})


@csrf_exempt
def trip_list(request):
    # GET → public trips (no owner data)
    if request.method == 'GET':
        
        trips = Trip.objects.all()

        result = []
        for trip in trips:
            result.append({
                "id": trip.id,
                "destination": trip.destination,
                "start_date": str(trip.start_date),
                "end_date": str(trip.end_date),
                "budget": trip.budget,
                "looking_for": trip.looking_for,
            })

        return JsonResponse(result, safe=False)

    # POST → login required
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Login required"}, status=401)

        data = json.loads(request.body)

        Trip.objects.create(
            owner=request.user,  
            destination=data.get('destination'),
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            budget=data.get('budget'),
            looking_for=data.get('looking_for'),
        )

        return JsonResponse({"message": "Trip created successfully"}, status=201)
