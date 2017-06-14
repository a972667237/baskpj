from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BaskUser
from django.http import HttpResponse
import json

# Create your views here.
class SignUp(View):
    def get(self, requests):
        return HttpResponse("Hello world")
    def post(self, requests):
        email = requests.POST['email']
        password = requests.POST['password']
        nick = requests.POST['nick']
        new_user = User.objects.create_user(email, email, password)
        user = BaskUser.objects.create(user = new_user, nick = nick)
        user_info = {
            'user': user.nick,
            'status': 'success'
        }
        return HttpResponse(json.dumps(user_info), content_type="Application/json")

class Signin(View):
    def get(self, requests):
        return HttpResponse("Hello world")
    def post(self, requests):
        email = requests.POST['email']
        password = requests.POST['password']
        user = authenticate(username=email, password=password)
        if not user:
            user_info = {
                'user': "null",
                'status': 'fail'
            }
            return HttpResponse(json.dumps(user_info), content_type="Application/json")
        login(requests, user)
        user = BaskUser.objects.get(user=user)
        user_info = {
            'user': user.nick,
            'status': 'success'
        }
        return HttpResponse(json.dumps(user_info), content_type="Application/json")

class SignOut(View):
    def get(self, requests):
        return HttpResponse("error")
    def post(self, requests):
        logout(requests)
        return HttpResponse('success')

def getUser(requests):
    user = requests.user
    try:
        user = BaskUser.objects.get(user=user)
    except:
        user_info = {
            'user': "null",
            'status': 'fail'
        }
        return HttpResponse(json.dumps(user_info), content_type="Application/json")
    user_info = {
        'user': user.nick,
        'status': 'success'
    }
    return HttpResponse(json.dumps(user_info), content_type="Application/json")
