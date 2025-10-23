from django.forms import ModelForm
from application1.models import StudentTable
from django.core.exceptions import ValidationError


class StudentForm(ModelForm):
    class Meta:
        model = StudentTable
        fields = "__all__"
        error_messages = {
            # This helps in giving customized error messages instead of default one's
            "name": {
                "required": "Name field cannot be left blank.",
                "max_length": "Name cannot exceed 50 characters.",
            },
            "email": {
                "required": "Email is mandatory.",
                "invalid": "Enter a valid email address.",
            },
            "phone": {
                "required": "Phone number is required.",
                "max_length": "Phone number must be 10 digits only.",
            },
        }
    
    # This is a Validation Error handling logic [Server Side] using cleaned_data
    # cleaned_data is to access validated data safely [through ModelForm]
    # and perform custom validation operations


    # Django expects field level validators follow the same pattern
    # name ---> clean_name
    # email -----> clean_email
    # No other method name is allowed

    def clean_name(self):
        # self here reference to the form instance of the class
        name = self.cleaned_data.get("name")
        namesplit = name.split()

        for part in namesplit:
            if not (part[0].isupper() and part[1:].islower()):
                raise ValidationError("Each part of the name should start with a capital letter.")
    
        return name
    
    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if len(phone) != 10:
            raise ValidationError("Phone Number must be of 10 digits")
        
        return phone 
    

    # While clean_<field>() validates one field at a time,
    # clean() lets you validate across multiple fields.
    # Typical use: check logical relationships between fields.
    def clean(self):
        cleaned_data = super().clean()  # always call super()
        name = cleaned_data.get("name")
        phone = cleaned_data.get("phone")

        if name and phone:
            if name.lower().startswith("a") and str(phone).startswith("9"):
                raise ValidationError("Name starting with 'A' cannot have a phone number that starts with 9.")
    
        return cleaned_data

