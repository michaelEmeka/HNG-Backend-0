from django.http import JsonResponse
import json
from datetime import datetime

def home(request):
    if request.method == "GET":
        json_string = {
            "email": "mikelonu15@gmail.com",
            "current_datetime": f"{datetime.now()}",
            "github_url": "https://github.com/michaelEmeka/HNG-Backend-0.git",
        }
    return JsonResponse(json_string)