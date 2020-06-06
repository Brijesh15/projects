from django.db import models

# Create your models here.

class company_list(models.Model):

    class Meta:
        db_table = "company_list"

    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)

class PhonePe(models.Model):

    class Meta:
        db_table = "PhonePe"

    company_id = models.IntegerField()
    scanned_result = models.CharField(max_length=50)
    qrid = models.CharField(max_length=500)
    qrcode = models.CharField(max_length=500)
    lot_number = models.CharField(max_length=20)
    created_at = models.IntegerField()
    updated_at = models.IntegerField(null=True)

class Airtel(models.Model):

    class Meta:
        db_table = "Airtel"

    company_id = models.IntegerField()
    scanned_result = models.CharField(max_length=50)
    VPA = models.CharField(max_length=500)
    qrcode = models.CharField(max_length=500)
    created_at = models.IntegerField()
    updated_at = models.IntegerField(null=True)

class Mudra(models.Model):

    class Meta:
        db_table = "Mudra"

    company_id = models.IntegerField()
    scanned_result = models.CharField(max_length=50)
    qrid = models.CharField(max_length=500)
    qrcode = models.CharField(max_length=500)
    lot_number = models.CharField(max_length=20)
    created_at = models.IntegerField()
    updated_at = models.IntegerField(null=True)

class Paytm(models.Model):

    class Meta:
        db_table = "Paytm"

    company_id = models.IntegerField()
    scanned_result = models.CharField(max_length=50)
    qrid = models.CharField(max_length=500)
    qrcode = models.CharField(max_length=500)
    lot_number = models.CharField(max_length=20)
    created_at = models.IntegerField()
    updated_at = models.IntegerField(null=True)

class HomePageView():

    def insertData(self):

        com_name = ["PhonePe", "Airtel", "Paytm", "Mudra"]
        for company in com_name:
            if company_list.objects.filter(company_name=company):
                continue
            c = company_list(company_name=company)
            c.save()

