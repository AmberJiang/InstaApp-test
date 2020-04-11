from django.urls import path
from . import views

urlpatterns = [
    path('',views.HelloDjango.as_view())
    #app level url to handle url for helloDango view
]