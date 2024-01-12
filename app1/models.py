from django.db import models

# Create your models here.
class Doctor(models.Model):
    did=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=150, verbose_name='Doctor Name')
    dqua=models.CharField(max_length=255, verbose_name='Doctor Qualification')
    aboutdoc=models.TextField(verbose_name='About Doctor')

class Schedule(models.Model):
    sid=models.AutoField(primary_key=True)
    days=models.CharField(max_length=200, verbose_name='Available Days')
    t_slot=models.CharField(max_length=200)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Select Doctor')