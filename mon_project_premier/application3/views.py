from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse(
        """
<h1>This is a Application Level URL</h1>
"""
    )
def welcome(request):
    return HttpResponse(
        """
<h1>Welcome</h1>
"""
    )
def template_function(request):
    return render(request, "welcome.html")