from django.db import models
import string
import random
from django.contrib.auth.models import User
from django.contrib.gis.geoip2 import GeoIP2

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
    url_count = models.IntegerField(default=0)

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
        print(f"rand_string : {str_pool}")
        # return ("".join([random.choices(str_pool) for i in range(6)])).lower()
        return "".join(random.choices(str_pool, k=6)).lower()
    
    def rand_letter():
        str_pool = string.ascii_letters
        print(f"rand_letter : {str_pool}")
        return random.choice(str_pool).lower()
    
    nick_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categorys, on_delete=models.DO_NOTHING, null=True)
    prefix = models.CharField(max_length=50, default=rand_letter)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    click = models.BigIntegerField(default=0)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    expired_at = models.DateTimeField(null=True)

    class Meta:
        indexes = [
            models.Index(
                fields=["prefix", "shortened_url"],
            ),
        ]

    def clicked(self):
        self.click += 1
        self.save()


class Statistic(TimeStampedModel):
    class ApproachDevice(models.TextChoices):
        PC = "pc"
        MOBILE = "mobile"
        TABLET = "tablet"
    
    shortened_url = models.ForeignKey(ShorteneUrls, on_delete=models.CASCADE)
    ip = models.CharField(max_length=15)
    web_browser = models.CharField(max_length=50)
    device = models.CharField(max_length=6, choices=ApproachDevice.choices)
    device_os = models.CharField(max_length=30)
    country_code = models.CharField(max_length=2, default="XX")
    country_name = models.CharField(max_length=50, default="Unknown")

    def record(self, request, url: ShorteneUrls):
        self.shortened_url = url
        print(f"url : {url.target_url}")
        self.ip = request.META["REMOTE_ADDR"]
        self.web_browser = request.user_agent.browser.family
        self.device = self.ApproachDevice.MOBILE if request.user_agent.is_mobile else self.ApproachDevice.TABLET if request.user_agent.is_tablet else self.ApproachDevice.PC
        self.device_os = request.user_agent.os.family
        try:
            country = GeoIP2().country(self.ip)
            self.country_code = country.get("country_code", "XX")
            self.country_name = country.get("country_name", "Unknown")
        except:
            pass
        url.clicked()
        self.save()



    
