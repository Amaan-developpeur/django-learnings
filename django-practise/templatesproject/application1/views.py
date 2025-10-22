from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, "welcome.html")

def home(request):
    data = {
        "names": ["Amaan", "charles"],
        "age": [23, 24]
    }
    final_data = {
    "people": zip(data["names"], data["age"])
}
    return render(request, "home.html", context=final_data)

def conditional(request):
    dicte = {
        'n' : 10
    }
    return render(request, "welcome2.html", context=dicte)

def display_image(request):
    return render(request, "test_image.html")

def display_link(request):
    return render(request, "click.html")

def view1(request):
    msg = "<h1>This is View 1</h1>"
    return HttpResponse(msg)

def view2(request):
    msg = "<h1>This is View 2</h1>"
    return HttpResponse(msg)

def view3(request):
    return render(request, "index.html")

def input_html(request):
    return render(request, "input_html.html")

def output_html(request):
    name = request.GET.get("name", "")
    context = {"name": name}
    print("DEBUG:", name)
    return render(request, "output_html.html", context)

def calci_html(request):
    return render(request, "calci_home.html")

def calculate(request):
    num1 = int(request.GET.get("num1", 0))
    num2 = int(request.GET.get("num2", 0))
    button = request.GET.get("button")

    if button == "ADD":
        result = num1 + num2
    elif button == "SUB":
        result = num1 - num2
    elif button == "MUL":
        result = num1 * num2
    elif button == "DIV":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"

    return render(request, "calciresult.html", {"result": result})
