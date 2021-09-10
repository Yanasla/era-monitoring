from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Test(User):
    fill_num = models.IntegerField(default=0)
    batch = models.IntegerField(default=0)
    strength = models.DecimalField(max_digits=15, decimal_places=4)
    density = models.DecimalField(max_digits=15, decimal_places=4)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
    	return self.title
    class Meta: 
        verbose_name = 'Проба'
        verbose_name_plural = 'Пробы'

class Operator(Test):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    
    def __str__(self):
    	return self.title
    class Meta: 
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'