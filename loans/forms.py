from django.forms import ModelForm, ModelChoiceField, ChoiceField, Select, TextInput, NumberInput, Textarea
from .models import UserModel, LoanApplication, LoanReview


DURATION = (
    ('3 months', '3 months'),
    ('6 months', '6 months'),
    ('12 months', '12 months'),
    ('18 months', '18 months'),
    ('24 months', '24 months'),
)

STATUS = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
)

class ApplicationForm(ModelForm):
    duration = ChoiceField(choices=DURATION, widget=Select(attrs={"class":"form-control"}))
    recipient = ModelChoiceField(queryset=UserModel.objects.all(), widget=Select(attrs={"class":"form-control"}))
    
    class Meta:
        model = LoanApplication
        fields = ["applicant_name", "applicant_account", "amount", "duration", "account_officer", "recipient"]
        widgets = {
            "applicant_name": TextInput(attrs={"class":"form-control"}),
            "applicant_account": NumberInput(attrs={"class":"form-control"}),
            "amount": NumberInput(attrs={"class":"form-control"}),
            # "collateral": FileInput(attrs={"class":"form-control"}),
            "account_officer": TextInput(attrs={"class":"form-control"}),
        }


class ApplicationUpdateForm(ModelForm):
    duration = ChoiceField(choices=DURATION, widget=Select(attrs={"class":"form-control"}))
    status = ChoiceField(choices=STATUS, widget=Select(attrs={"class":"form-control"}))
    recipient = ModelChoiceField(queryset=UserModel.objects.all(), widget=Select(attrs={"class":"form-control"}))
    
    class Meta:
        model = LoanApplication
        fields = "__all__"
        widgets = {
            "applicant_name": TextInput(attrs={"class":"form-control"}),
            "applicant_account": NumberInput(attrs={"class":"form-control"}),
            "amount": NumberInput(attrs={"class":"form-control"}),
            # "collateral": FileInput(attrs={"class":"form-control"}),
            "account_officer": TextInput(attrs={"class":"form-control"}),
            "comment": Textarea(attrs={"class":"form-control", "rows":3}),
        }


class ReviewForm(ModelForm):
    status = ChoiceField(choices=STATUS, widget=Select(attrs={"class":"form-control mb-3"}))
    recipient = ModelChoiceField(queryset=UserModel.objects.all(), widget=Select(attrs={"class":"form-control mb-3"}))
    
    class Meta:
        model = LoanReview
        fields = '__all__'
        labels = {'official': '', 'applicant': ''}
        widgets = {
            "official": TextInput(attrs={"class":"form-control", "id":"official", "value": "", "type":"hidden"}),
            "applicant": TextInput(attrs={"class":"form-control", "id":"applicant", "value": "", "type":"hidden"}),
            "comment": Textarea(attrs={"class":"form-control mb-3", "rows":3}),
        }
