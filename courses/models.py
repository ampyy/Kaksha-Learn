from django.db import models
from django.core.validators import RegexValidator


class Courses(models.Model):
    video = models.CharField(max_length=1000, null=False)
    title = models.CharField(max_length=22, null=False)
    cour_desc = models.TextField(max_length=1500, null=False)
    cour_time = models.CharField(max_length=255, null=False)
    amount = models.PositiveIntegerField(default=0)


class ContactUs(models.Model):
    name = models.CharField(null=False, max_length=50)
    number = models.BigIntegerField(max_length=10)
    message = models.CharField(null=False, max_length=1000)


class Transaction(models.Model):
    name = models.CharField(max_length=50, null=False)
    made_on = models.DateTimeField(auto_now_add=True)
    number = models.BigIntegerField(max_length=10)
    courses = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.CharField(max_length=10)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
                            

class Bought(models.Model):
    name = models.CharField(max_length=50, null=False)
    number = models.BigIntegerField(max_length=10)
    paid = models.CharField(max_length=10)


class Preview(models.Model):
    heading = models.CharField(max_length=50, null=False)
    head1 = models.CharField(max_length=50, null=False)
    head2 = models.CharField(max_length=50, null=False)
    head3 = models.CharField(max_length=50, null=False)
    head4 = models.CharField(max_length=50, null=False)
    head5 = models.CharField(max_length=50, null=False)
    iframe1 = models.CharField(max_length=1000, null=False)
    iframe2 = models.CharField(max_length=1000, null=False)
    iframe3 = models.CharField(max_length=1000, null=False)
    img1 = models.CharField(max_length=1000, null=False)
    img2 = models.CharField(max_length=1000, null=False)


