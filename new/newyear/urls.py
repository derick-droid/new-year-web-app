from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>", views.index, name = "index"),
    path("newyear/", views.index, name = "index")
    
]