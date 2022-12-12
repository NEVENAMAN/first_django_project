from django.shortcuts import render,HttpResponse

def display_surveys(request):
    return HttpResponse("placeholder to display all the surveys created")

def new_surveys(request):
    return HttpResponse("placeholder for users to add a new survey")


def index(request):
    return render(request,"index.html")
