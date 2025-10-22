from django.shortcuts import render
from django.http import HttpResponse
from .models import UserRegistration

# Create your views here.
def register_home(request):
    return render(request, "user_register.html")

def register_view(request):
    name = request.POST.get("name")
    username = request.POST.get("username")
    password = request.POST.get("pw")
    UserRegistration.objects.create(name=name, username=username, password=password)
    return HttpResponse("""
<h1>User Registered Successfully</h1>
"""
    
    )