from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),  # Just for getting details about Project
]
