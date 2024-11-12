from django import forms
from django.core import validators


def sal(s):
    if s not in [10000,20000,30000,40000]:
        raise forms.ValidationError("salaroy 10000 0r 20 or 30 or 40")

class user_form(forms.Form):
    eno=forms.IntegerField()
    ename=forms.CharField()
    esal=forms.IntegerField(validators=[sal])
    eaddr=forms.CharField(widget=forms.Textarea)

    #form clean validation
    def clean(self):
        total=super().clean()
        name=total["ename"]
        if len(name)<4:
            raise forms.ValidationError("minimu 5 charecter")




    #forms validations
    '''def clean_ename(self):
        name=self.cleaned_data["ename"]
        if len(name)>4:
            return name
            
        raise forms.ValidationError("more then 5 charecters")'''
