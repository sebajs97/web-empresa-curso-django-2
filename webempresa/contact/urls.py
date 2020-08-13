from django.urls import path
from . import views

urlpatterns = [
    # Path de contacts
    path('', views.contact, name="contact"),
]
