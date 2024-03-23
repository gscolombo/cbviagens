from cbviagens_api.utils import getResponse
from .models import Travel
from .serializers import TravelSerializer
from datetime import datetime, timedelta

from django.http import JsonResponse, HttpRequest

def test(req: HttpRequest)-> JsonResponse:
    """Endpoint for testing the API"""
    return JsonResponse(getResponse(ok=True, code=200, data={"message": "All good!"}))

def destinations(req: HttpRequest)-> JsonResponse:
    """Returns a JSON response containing a list of unique destinations from the 'Travel' model data."""
    try :
        destinations: list[str] = []
        for t in TravelSerializer(Travel.objects.all()).data['travels']:
            if t['city'] not in destinations:
                destinations.append(t['city'])
        return JsonResponse(getResponse(ok=True, code=200, data={"destinations": destinations}))
    except:
        return JsonResponse(getResponse(ok=False, code=400, data={"error": "Sorry, we could not process your request."})) 
    

def crud(req: HttpRequest):
    """Processes CRUD requests based on method of the `req` parameter."""
    try:
        method_handlers = {
            "GET": get,
            "POST": lambda: JsonResponse(getResponse(ok=False, code=405, data={"error": "Method not allowed."})),
            "UPDATE": lambda: JsonResponse(getResponse(ok=False, code=405, data={"error": "Method not allowed."})),
            "DELETE": lambda: JsonResponse(getResponse(ok=False, code=405, data={"error": "Method not allowed."})),
        }
        return (JsonResponse)(method_handlers[req.method](req))
    except:
        return JsonResponse(getResponse(ok=False, code=400, data={"error": "Sorry, we could not process your request."}))

def get(req: HttpRequest):
    """Extracts and returns data from the 'Travel' model based on the query parameters, if any."""
    query: dict = req.GET.dict()
    if not query:
        travels = TravelSerializer(Travel.objects.all()).data
        return getResponse(ok=True, code=200, data=travels)
    else:
        if 'departureDate' in query:
            departureDate = datetime.strptime(query.pop('departureDate'), "%Y-%m-%d")
        travelsData = TravelSerializer(Travel.objects.filter(**query)).data
        if departureDate:
            # Add estimated arrival date in response data
            arrivalDate = lambda date, t : (date + timedelta(hours=t)).strftime("%d/%m/%Y")
            arrivals = [arrivalDate(departureDate, t['duration']) for t in travelsData['travels']]
            travelsData = [
                {
                    **t, 
                    'estimated_arrival_date': 'No mesmo dia' if arrivals[i] == departureDate.strftime("%d/%m/%Y") else arrivals[i]
                } 
                for i, t in enumerate(travelsData['travels'])]
        return getResponse(ok=True, code=200, data={"travels": travelsData})
    
# TODO: implements the actions for the POST, UPDATE e DELETE methods
def post():
    pass

def update():
    pass

def delete():
    pass