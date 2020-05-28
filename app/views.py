from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from app.models import *
import json
def index(request):
    user=UserProfile.objects.create(username='lee',password='123456')
    all=UserProfile.objects.all().values('username','password')
    print(all)
    res=list(all)
    return HttpResponse(json.dumps(res))
