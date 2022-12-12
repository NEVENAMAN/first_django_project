from django.shortcuts import render,HttpResponse

def two_app(request):
    return HttpResponse("app two")

