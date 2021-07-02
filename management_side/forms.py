from django.forms import ModelForm

from .models import *

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields="__all__"
        exclude = ['manager' ]


# class Book_status_condition_form(ModelForm):
#     class Meta:
#         model = Book
#         fields="status","condition"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields ="__all__"
        exclude = ['user' ]


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields ="__all__"
        exclude = ['user' ]


