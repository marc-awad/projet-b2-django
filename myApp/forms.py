from django import forms
from .models import Conges

class AskConges(forms.ModelForm):
    class Meta:
        model = Conges
        fields = ['name', 'lastname', 'email', 'date','end_date', 'reason']