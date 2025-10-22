from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class HelloView(View):
    def get(self, request):
        return HttpResponse(
            """
<h1>Hello this is class based view</h1>
"""
        )
