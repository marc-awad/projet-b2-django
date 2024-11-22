from django import forms
from .models import Conges
# import re
# from django.core.exceptions import ValidationError

# Regex pas nécessaire car Django fait déjà la validation de la date pour nous
# def validate_date(date):
#     regex = r'(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})'
#     if not re.match(regex, date):
#         raise ValidationError("Date is not valid")

class AskConges(forms.ModelForm):
    class Meta:
        model = Conges
        fields = ['name', 'lastname', 'email', 'date','end_date', 'reason']

    #Code lié au regex plus haut
    # date = forms.DateField(validators=[validate_date])
    # end_date = forms.DateField(validators=[validate_date])

class AdminstratorConnection(forms.Form):
    username = forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput())