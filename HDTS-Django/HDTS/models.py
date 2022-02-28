#import datetime

from djongo import models
#from django.utils import timezone
#from django.contrib import admin
#from django.contrib.auth.models import User


class HardDrive(models.Model):
    
    creationDate = models.DateField(db_column='Creation Date',  blank=True, null=True)
    serialNo = models.IntegerField(db_column='Serial Number', blank=True, null=True)
    manufacturer = models.CharField(db_column='Manufacturer',max_length=50,  blank=True, null=True)
    modelNo = models.IntegerField(db_column='Model Number',  blank=True, null=True)
    hdType = models.CharField(db_column=' Hard Drive Type',max_length=50,  blank=True, null=True)
    connPort = models.CharField(db_column=' Hard Drive Connection Port',max_length=50,  blank=True, null=True)
    hdSize = models.CharField(db_column='Hard Drive Size',max_length=50,  blank=True, null=True)
    hdClass = models.CharField(db_column=' Hard Drive Classification',max_length=50,  blank=True, null=True)
    justiClass = models.FileField(db_column='Justification for Classification Change',  blank=True, null=True)
    imageVerID = models.IntegerField(db_column='Image Version ID',  blank=True, null=True)
    btStatus = models.BooleanField(db_column='Boot Test Passed?',  blank=True, null=True)
    btExpDate = models.DateField(db_column='Boot Expiration Date',  blank=True, null=True)
    hdStatus = models.CharField(db_column='HD Status',max_length=50,  blank=True, null=True)
    justiStatus = models.FileField(db_column='Justification Change Status',  blank=True, null=True)
    issueDate = models.DateField(db_column='Issue Date',  blank=True, null=True)
    expectRetDate = models.DateField(db_column='Expected Returned Date',  blank=True, null=True)
    justiRetDate = models.FileField(db_column='Justification Change Return Date',  blank=True, null=True)
    actualRetDate = models.DateField(db_column='Actual Returned Date',  blank=True, null=True)
    modDate = models.DateField(db_column='Modified Date',  blank=True, null=True)    

    class Meta:
        managed = False
        db_table = 'harddrive'



