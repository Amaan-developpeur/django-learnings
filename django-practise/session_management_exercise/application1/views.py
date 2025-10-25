from django.shortcuts import render
from django.http import HttpResponse
from application1.models import EmployeeTable
from application1.forms import EmployeeForm

# Create your views here.
def crud(request):
    msg = ""
    form = EmployeeForm(request.POST or None)
    button = request.POST.get("button")
    visits = request.session.get("visits", 0) + 1 # <--- A library that Django gives you to store data per user session.
    request.session["visits"] = visits # <---- Now we store the updated visit count back into the session.
    # This ensures that the next time the same user makes a request, request.session.get("visits") will give the new count.

    if request.method == "POST":
        # CREATE
        if button == "Create":
            if form.is_valid():
                form.save()
                msg = "Employee created successfully!"
                request.session["last_action"] = msg
            else:
                msg = "Invalid data submitted."
                request.session["last_action"] = msg

        # RETRIEVE
        elif button == "Retrieve":
            email = request.POST.get("email")
            try:
                emp = EmployeeTable.objects.get(email=email)
                form = EmployeeForm(instance=emp)
                msg = f"Record found for {emp.name}"
                request.session["last_action"] = msg
            except EmployeeTable.DoesNotExist:
                msg = "Employee not found."
                request.session["last_action"] = msg

        # UPDATE
        elif button == "Update":
            email = request.POST.get("email")
            try:
                emp = EmployeeTable.objects.get(email=email)
                form = EmployeeForm(request.POST, instance=emp)
                if form.is_valid():
                    form.save()
                    msg = f"{emp.name}'s record updated successfully!"
                    request.session["last_action"] = msg
            except EmployeeTable.DoesNotExist:
                msg = "Employee not found for update."
                request.session["last_action"] = msg

        # DELETE
        elif button == "Delete":
            email = request.POST.get("email")
            try:
                emp = EmployeeTable.objects.get(email=email)
                emp.delete()
                msg = "Employee deleted successfully!"
                form = EmployeeForm()  # clear form
                request.session["last_action"] = msg
            except EmployeeTable.DoesNotExist:
                msg = "Employee not found for deletion."
                request.session["last_action"] = msg

    return render(request, "crud.html", {"form": form, "msg": msg, "visits": visits, "last_action": request.session.get("last_action", "")})

