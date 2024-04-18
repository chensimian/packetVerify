from django.db import models
# from api.models import *

class RIB_Model(models.Model):
    id=models.AutoField(primary_key=True)
    deviceId = models.ForeignKey('api.deviceModel', on_delete=models.CASCADE)
    srcIP = models.CharField(max_length=17)
    dstIP = models.CharField(max_length=17)
    nextHop = models.CharField(max_length=15)
    inInterfaceId = models.IntegerField()
    outInterfaceId = models.IntegerField()

class FIB_Model(models.Model):
    id = models.AutoField(primary_key=True)
    deviceId = models.ForeignKey('api.deviceModel', on_delete=models.CASCADE)
    dstIP = models.CharField(max_length=17)
    outInterfaceId = models.CharField(max_length=15)

class verifyTable(models.Model):
    id = models.AutoField(primary_key=True)
    deviceId = models.ForeignKey('api.deviceModel', on_delete=models.CASCADE)
    srcIP = models.CharField(max_length=17)
    inInterfaceId = models.CharField(max_length=15)