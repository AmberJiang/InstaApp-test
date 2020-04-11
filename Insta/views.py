from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#Inherit TemplateView class from django view
class HelloDjango(TemplateView):
        template_name = 'home.html'
