from django.forms import ModelForm

from .models import Issue,Customer,Manager

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields="__all__"



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


