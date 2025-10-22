from django.forms import ModelForm
from application1.models import EmployeeTable

class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeTable
        fields = "__all__"