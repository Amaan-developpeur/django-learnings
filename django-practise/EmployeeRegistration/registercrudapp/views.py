from django.shortcuts import render
from django.http import HttpResponse
from registercrudapp.models import EmployeeRegistration
from django.views.generic import ListView

# Create your views here.
def register_form(request):
    return render(request, "register_form.html")


# ---- Helper function for CREATE operation ----
def handle_create(name, username, password):
    """Handles registration logic for new employees."""
    if EmployeeRegistration.objects.filter(username=username).exists():
        return "Username already exists."
    EmployeeRegistration.objects.create(
        name=name, username=username, password=password
    )
    return "User Registered Successfully!"

def handle_update(name, username, password):
    if EmployeeRegistration.objects.filter(username=username).exists():
        actual_password = EmployeeRegistration.objects.get(username=username).password
        if actual_password == password:
            EmployeeRegistration.objects.filter(username=username).update(
            name=name, username=username, password=password
        )
            return "User Information Updated Successfully"
        else:
            return "Password is incorrect"
        
    
    else:
        return "User does not exist"
    
def handle_delete(name, username, password):
    if EmployeeRegistration.objects.filter(username=username).exists():
        EmployeeRegistration.objects.filter(username=username).delete()
        return f"User {name} with id {username} has been successfully deleted"
    else:
        return "User does not exist"
    
def handle_retrieve(name, username, password):
    if EmployeeRegistration.objects.filter(username=username).exists():
        user = EmployeeRegistration.objects.get(username=username)
        if user.name == name and user.password == password:
            return [user.name, user.username, user.password]
        else:
            return "Password or Name is incorrect"
    else:
        return "Username does not exist"




# ---- Main CRUD handler ----
def crud_operations(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("pw")
        button = request.POST.get("button")

        if button == "Register/Create":
            msg = handle_create(name, username, password)
            return render(request, "create.html", {"msg": msg})
        
        elif button == "Update":
            msg = handle_update(name=name, username=username, password=password)
            return render(request, "update.html", {"msg":msg})
        
        elif button == "Retreive":
            msg = handle_retrieve(name=name, username=username, password=password)
            return render(request, "retreive.html", {"msg":msg})
        
        elif button == "Delete":
            msg = handle_delete(name=name, username=username, password=password)
            return render(request, "delete.html", {"msg":msg})
        else:
            msg = "Unknown operation."

        
    
        

    return render(request, "register_form.html")


# Class Based View [List View]
class EmployeeListView(ListView):
    # Assigning the model
    # Django fetches the details automatically
    model = EmployeeRegistration
    template_name = "employee_list.html"
    context_object_name = "employees"

from django.views.generic import CreateView
from registercrudapp.models import EmployeeTable

class EmployeeCreateView(CreateView):
    model = EmployeeTable
    fields = ['name', 'empid', 'salary']       # form fields to show
    template_name = "create_employee.html"     # your HTML form
    success_url = "/employees/"                # redirect after creation