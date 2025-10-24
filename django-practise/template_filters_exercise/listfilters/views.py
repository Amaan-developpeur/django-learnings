from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_filters_demo(request):
    students = ["Alice", "Bob", "Charlie", "David", "Zara"]
    context = {
        'students': students
    }
    return render(request, 'list_filters_demo.html', context)

