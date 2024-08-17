from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member as m
# Create your views here.
def members(request):
    allmembers=m.objects.all().values()

    temp =loader.get_template('all_members.html')
    return HttpResponse(temp.render({'allmembers':allmembers},request))
def details(request, id):
    me=m.objects.get(id=id)
    temp=loader.get_template('details.html')
    return HttpResponse(temp.render({'m':me},request))
def main(request):
    temp=loader.get_template("main.html")
    return HttpResponse(temp.render())
def testing(request,num):
    f=m.objects.all().values()
    temp=loader.get_template("testing.html")
    data ={
        'f':f,
        'greeting':num
    }
    return HttpResponse(temp.render(data,request))