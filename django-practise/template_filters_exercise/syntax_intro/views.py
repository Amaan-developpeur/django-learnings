from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def syntax_intro(request):
    data = {
        "name": "mohammed amaan"
    }
    return render(request, "syntax.html", context=data)




