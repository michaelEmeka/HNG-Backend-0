import requests

url = "https://hng-backend-0-1njc.onrender.com/api/get_intern_detail"

response = requests.get(url)
print(response.status_code)
