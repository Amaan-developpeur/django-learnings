from django.urls import path
from . import views

urlpatterns = [
    path("", views.display),
    path("welcome/", views.welcome),
    path("pagehtml/", views.template_function)
]
# "" means this is the default page of application3