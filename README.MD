This project is a simple API in fulfilment of the HNG intership level 0 project.
It receives a GET request via an API endpoint and send a JSON response, and handles HTTP status code.

API enpoint:
https://hng-backend-0-1njc.onrender.com/

JSON Response Format:
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "<https://github.com/yourusername/your-repo>"
}

Response status codes
-on success:
HTTP_200_OK
-on failure:
HTTP_403_FORBIDDEN


Setup instructions
1. Clone software from github into local machine
2. Install dependencies (pip install -r requirements.txt) from root directory
3. Run server (python manage.py runserver)