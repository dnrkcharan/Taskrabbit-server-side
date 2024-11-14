from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
import json
# Token Authentication can be implemented here using the rest frame work. 
# we get the acess token and refresh token we describe the life span of the token in the settings.py file.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class LoginAPI(APIView):
    def post(self, request):
        request.body = json.loads(request.body)
        username = request.body.get('username')
        password = request.body.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            return HttpResponse("Auth is sucessful")
        else:
            # No backend authenticated the credentials
            return HttpResponse("Login Failed")
        return HttpResponse("Hello, world. You're at Login.")


class SignupAPI(APIView):
    def post(self, request):
        print(request.body)
        request.body = json.loads(request.body)
        username = request.body.get('username')
        password = request.body.get('password')
        email = request.body.get('email')

        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse("Hello, world. Your signup was sucessful.")