from django import forms
from models import *

class SessionForm(forms.Form):
    customer = forms.CharField()
    model = forms.CharField()

class WorkOrderForm(forms.ModelForm):

    class Meta:
        model = WorkOrder
        exclude = ('session',)
        widgets = {
            "select": forms.Select(),
            "radio": forms.RadioSelect(),
            "checkbox": forms.CheckboxInput(),
        }
