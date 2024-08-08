from django.db import models
import string
import random
from django.contrib.auth.models import User

# Create your models here.

class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class PayPlan(TimeStampedModel):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    
class Organization(TimeStampedModel):
    class Industry(models.TextChoices):
        PERSONAL = "personal"
        RETAIL = "retail"
        MANUFACTURING = "manufacturing"
        IT = "it"
        OTHERS = "others"

    name = models.CharField(max_length=50)
    industry = models.CharField(max_length=15, choices=Industry.choices, default=Industry.OTHERS)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    Organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)

class EmailVerification(TimeStampedModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    key = models.CharField(max_length=100,null=True)
    verified = models.BooleanField(default=False)


class Categorys(TimeStampedModel):
    name = models.CharField(max_length=100)
    Organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    creator = models.ForeignKey(Users, on_delete=models.DO_NOTHING)



class ShorteneUrls(TimeStampedModel):
    class UrlCreatedVia(models.TextChoices): 
        WEBSITE = "web"
        TELEGRAM = "telegram"
    
    def rand_string():
        str_pool = string.digits + string.ascii_letters 
        # return ("".join([random.choices(str_pool) for i in range(6)])).lower()
        return "".join(random.choices(str_pool, k=6)).lower()
    
    nick_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categorys, on_delete=models.DO_NOTHING, null=True)
    prefix = models.CharField(max_length=50)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    expired_at = models.DateTimeField(null=True)

    
