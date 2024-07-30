from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PayPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
