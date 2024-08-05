from django.db import models
from django.contrib.auth.models import User
import string
import random

# Create your models here.

class PayPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)

class ShorteneUrls(models.Model):
    class UrlCreatedVia(models.TextChoices): 
        WEBSITE = "web"
        TELEGRAM = "telegram"
    
    def rand_string():
        str_pool = string.digits + string.ascii_letters 
        # return ("".join([random.choices(str_pool) for i in range(6)])).lower()
        return "".join(random.choices(str_pool, k=6)).lower()
    
    nick_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
