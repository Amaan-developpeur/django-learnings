from django.shortcuts import render
from django.http import HttpResponse
from application1.models import EmployeeTable
from application1.forms import EmployeeForm

# Create your views here.
def crud(request):
    msg = ""
    form = EmployeeForm(request.POST or None)
    button = request.POST.get("button")

    if request.method == "POST":
        # CREATE
        if button == "Create":
            if form.is_valid():
                form.save()
                msg = "Employee created successfully!"
            else:
                msg = "Invalid data submitted."

        # RETRIEVE
        elif button == "Retrieve":
            email = request.POST.get("email")
            try:
                emp = EmployeeTable.objects.get(email=email)
                form = EmployeeForm(instance=emp)
                msg = f"Record found for {emp.name}"
            except EmployeeTable.DoesNotExist:
                msg = "Employee not found."

        # UPDATE
        elif button == "Update":
            email = request.POST.get("email")
            try:
                emp = EmployeeTable.objects.get(email=email)
                form = EmployeeForm(request.POST, instance=emp)
                if form.is_valid():
                    form.save()
                    msg = f"{emp.name}'s record updated successfully!"
            except EmployeeTable.DoesNotExist:
                msg = "Employee not found for update."

        # DELETE
        elif button == "Delete":
            email = request.POST.get("email")
            try:
                emp = EmployeeTable.objects.get(email=email)
                emp.delete()
                msg = "Employee deleted successfully!"
                form = EmployeeForm()  # clear form
            except EmployeeTable.DoesNotExist:
                msg = "Employee not found for deletion."

    return render(request, "crud.html", {"form": form, "msg": msg})

