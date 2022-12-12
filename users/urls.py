from django.urls import path
from . import views

urlpatterns = [
    path('/register',views.create_new_user),
    path('/login',views.login_User),
    path('/users/new',views.new_user),
    path('/users',views.login_User),
]