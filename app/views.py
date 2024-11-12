from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.

def user(request):
    d=Employee.objects.all()
    #d=Employee.objects.filter(esal=40000) 
    #d=Employee.objects.filter(ename__startswith="a")
    da={"data":d}
    return render(request,"index.html",da)

def add_data(request):
    if request.method=="POST":
        en=request.POST["eno"]
        ena=request.POST["ename"]
        esa=request.POST["esal"]
        eadd=request.POST["eaddr"]
        d=Employee.objects.get_or_create(eno=en,ename=ena,esal=esa,eaddr=eadd)[0]
        d.save()
        return HttpResponse(d)
    else:
        return render(request,"addatahtmlform.html")
    


def data_forms(request):
    form=user_form()
    subbmit=False
    name=""
    if request.method=="POST":
        form=user_form(request.POST)
        if form.is_valid():
            n=form.cleaned_data["eno"]
            na=form.cleaned_data["ename"]
            sa=form.cleaned_data["esal"]
            ad=form.cleaned_data["eaddr"]
            name+=form.cleaned_data["ename"]
            subbmit=True
    return render(request,"django_forms.html",{"form":form,"subbmit":subbmit,"name":name})