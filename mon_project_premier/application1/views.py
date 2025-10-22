from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello, View is a Business Logic Implementation layer</h1>")

def bonjour(request):
    return HttpResponse(
        """
<h1>Bonjour, cest la phrase en francaise</h1>
"""
        
    )


