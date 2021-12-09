from django.db import models

class Sms(models.Model):
    sender = models.CharField(max_length=100)
    body = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    receiver = models.CharField(max_length=100)

class BatteryLevel(models.Model):
    batteryPct = models.FloatField()
    action = models.CharField(max_length=100)
    action_time = models.DateTimeField()