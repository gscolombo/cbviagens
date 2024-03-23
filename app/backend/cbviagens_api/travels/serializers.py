from .models import Travel
from django.db.models import QuerySet

class TravelSerializer:
    data: dict
    
    def __init__(self, t: QuerySet) -> None:
        travels = list(t.values())
        for travel in travels:
            t = travel['duration']
            travel['duration'] = t.days*24 + t.seconds // 3600 # Retrieve hours from timedelta
            # Fix for some specific problem due (I guess) to the UTF-8 enconding of SQLite
            # For more details, check out the following issue in StackOverflow
            # https://stackoverflow.com/questions/26290513/encoding-issue-s%C3%A3o-paulo-becomes-sc3a3o20paulo-then-s%C3%83%C2%A3o-paulo
            travel['city'] = travel['city'].replace("Ã£", 'ã') 
        
        self.data = {
            "travels": travels
        }