from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index),  # path to the website domain
    path('meetups/<slug:meetup_slug>', views.meetup_details), # page to render meet up details
]