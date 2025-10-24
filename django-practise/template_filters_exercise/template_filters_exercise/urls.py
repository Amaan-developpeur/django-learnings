"""
URL configuration for template_filters_exercise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from syntax_intro import views
from textfilters import views as v2
from numericfilters import views as v3
from listfilters import views as v4

urlpatterns = [
    path("admin/", admin.site.urls),
    path("syntax", views.syntax_intro, name="syntax"),
    path("textfilters", v2.textfilters, name="text"), 
    path("numericfilters", v3.numeric_filters, name="numeric"),
    path('listfilters/', v4.list_filters_demo, name='list_filters_demo'),
]
