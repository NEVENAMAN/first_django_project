from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('/surv',views.display_surveys),
    path('/surv/new',views.new_surveys),
]