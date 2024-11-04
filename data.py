import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysql.settings")

import django

django.setup()

from faker import Faker
import random
from app.models import *


data=Faker()

for i in range(10):
    en=random.randint(103,900)
    enam=data.name()
    esa=random.choice([10000,20000,30000,40000])
    eadd=data.address()
    
    Employee.objects.get_or_create(eno=en,ename=enam,esal=esa,eaddr=eadd)
    

