from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def numeric_filters(request):
    context = {
        'num1': 15,
        'num2': 4,
        'pi_value': 3.141592,
        'some_date': datetime(2025, 10, 24, 14, 30),
        'undefined_variable': None,
        'none_variable': None,
    }
    return render(request, 'numericfilters.html', context)
