from django.forms import ModelForm
from application1.models import StudentModel

class StudentForm(ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"

