from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView
from application1.models import EmployeeTable
from django.urls import reverse_lazy

# Create your views here.
class EmployeeCreateView(CreateView):
    model = EmployeeTable
    fields = "__all__"
    template_name = "create_employees.html"
    success_url = reverse_lazy("employee_list")


class EmployeeListView(ListView):
    model = EmployeeTable
    template_name = "list_employees.html"


class EmployeeUpdateView(UpdateView):
    model = EmployeeTable
    fields = "__all__"
    template_name = "update_employee.html"
    success_url = reverse_lazy("employee_list")