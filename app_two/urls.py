from django.urls import path
from . import views

urlpatterns = [
    path('',views.two_app),
]