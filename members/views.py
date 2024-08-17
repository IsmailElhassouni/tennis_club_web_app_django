from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member as m
# Create your views here.
def members(request):
    allmembers=m.objects.all().values()

    temp =loader.get_template('all_members.html')
    return HttpResponse(temp.render({'allmembers':allmembers},request))