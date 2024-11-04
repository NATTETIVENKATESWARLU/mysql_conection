from django.contrib import admin
from app.models import *
# Register your models here.
class Employee_inf(admin.ModelAdmin):
    list_display=["eno","ename","esal","eaddr"]

admin.site.register(Employee,Employee_inf)