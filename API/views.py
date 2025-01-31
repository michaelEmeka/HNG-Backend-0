from django.http import JsonResponse
from django.utils import timezone
import json
from datetime import datetime

def home(request):
    json_string = {}
    if request.method == "GET":
        json_string = {
            "email": "mikelonu15@gmail.com",
            "current_datetime": f"{timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')}",
            "github_url": "https://github.com/michaelEmeka/HNG-Backend-0.git",
        }
    return JsonResponse(json_string)