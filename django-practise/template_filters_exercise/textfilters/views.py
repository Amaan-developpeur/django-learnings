from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def textfilters(request):
    data = {
        "name": "Mohammed Amaan"
    }
    return render(request, "textfilters.html", context=data)
