from django.shortcuts import render
from django.http import HttpResponse
from application1.models import StudentTable
from application1.forms import StudentForm

# Create your views here.
def crud_function(request):
    msg = ""
    form = StudentForm(request.POST or None)
    button = request.POST.get("button")

    if request.method == "POST":
        if button == "CREATE":
            if form.is_valid():
                form.save()
                name = request.POST.get("name")
                emp = StudentTable.objects.get(name=name)
                msg = f"Student Record With Name {emp.name} Has Been Created"
            else:
                msg = "Form Data is Invalid"
        elif button == "UPDATE":
            email = request.POST.get("email")
            try:
                emp = StudentTable.objects.get(email=email)
                form = StudentForm(request.POST, instance=emp)
                msg = f"Record updated with name: {emp.name}"
            except StudentTable.DoesNotExist():
                msg = "Record Not Found"
        elif button == "RETREIVE":
            email = request.POST.get("email")
            try:
                if StudentTable.objects.filter(email=email).exists():
                    emp = StudentModel.objects.get(email=email)
                    form = StudentForm(instance=emp)
                    msg = f"Retreived Information shows here"
                else:
                    msg = "User does not exist"
            except StudentTable.DoesNotExist():
                msg = "Reccord not found"
        elif button == "DELETE":
            email = request.POST.get("email")
            try:
                if StudentTable.objects.filter(email=email).exists():
                    StudentTable.objects.filter(email=email).delete()
                    form = StudentForm()
                    msg = f"Student Information Deleted"
                else:
                    msg = "User does not exist"
            except StudentTable.DoesNotExist():
                msg = "Reccord not found"
    return render(request, "home.html", {"form": form, "msg":msg})


