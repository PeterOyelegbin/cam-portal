from django.forms import ModelForm, ChoiceField, Select, TextInput, EmailInput, PasswordInput
from .models import UserModel


ROLE = (('BM', 'BM'), ('CREDIT', 'CREDIT'), ('CSO', 'CSO'),
    ('IT', 'IT'), ('MD', 'MD'), ('RM', 'RM'),
)

class UserCreationForm(ModelForm):
    role = ChoiceField(choices=ROLE, widget=Select(attrs={"class":"form-control"}))
    
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "role", "branch", "email", "password"]
        widgets = {
            "first_name": TextInput(attrs={"class":"form-control"}),
            "last_name": TextInput(attrs={"class":"form-control"}),
            "branch": TextInput(attrs={"class":"form-control"}),
            "email": EmailInput(attrs={"class":"form-control"}),
            "password": PasswordInput(attrs={"class":"form-control"}), 
        }



class UserUpdateForm(ModelForm):
    role = ChoiceField(choices=ROLE, widget=Select(attrs={"class":"form-control"}))
    
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "role", "branch"]
        widgets = {
            "first_name": TextInput(attrs={"class":"form-control"}),
            "last_name": TextInput(attrs={"class":"form-control"}),
            "branch": TextInput(attrs={"class":"form-control"}), 
        }
