from django import forms
from skippings.models import Person

class RegisterForm(forms.ModelForm):
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    age = forms.IntegerField()
    reason = forms.CharField(required=True)

    class Meta:
        model = Person
        fields = ("firstname", "lastname", "age", "reason",)
    