from django.shortcuts import render,redirect ,HttpResponse

def create_new_user(request):
    return HttpResponse("placeholder for users to create a new user record")

def login_User(request):
    return HttpResponse("placeholder for users to log in")

def new_user(request):
    return redirect('/register')

def list_users(request):
    return HttpResponse("placeholder to later display all the list of users")