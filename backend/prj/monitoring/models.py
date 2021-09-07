from django.db import models

from django.contrib.auth.models import User

class Test(User):
    fill_num = models.IntegerField(default=0)
    batch = models.IntegerField(default=0)
    strength = models.DecimalField(max_digits=15, decimal_places=4)
    density = models.DecimalField(max_digits=15, decimal_places=4)
    timestamp = models.TimeField(auto_now=True)

class Operator(Test):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250), default='')
    class Meta: 
        verbose_name = 'Operator'
        verbose_name_plural = 'My images'