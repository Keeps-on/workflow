from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from app.models import *

def index(request):
    user=UserProfile.objects.create(username='lee',password='123456')
    all=UserProfile.objects.all().values()
    print(all)
    return HttpResponse('this is dev-lee')
