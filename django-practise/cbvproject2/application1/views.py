from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import EmployeeTable

# Create your views here.
class EmployeeTable(ListView):
    model = EmployeeTable
    template_name = "employee_list.html"
    context_object_name = "employees"
