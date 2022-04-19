from djongo import models
from .choices import *
import datetime

'''
The Hard Drive Class has all the attributes from the SRS Real World Object Requirements
    The Object is stored in the 'harddrive' collection on our Mongo database
    There are three types of files for the Hard Drives. 
        For the following Hard Drive fields their files are stored in the following directories
            -justiClass: '/media/Justification_Class_Change/'
            -justiStatus:'/media/Justification_Status_Change/'
            -justiRetDate: '/media/Justification_Return_Date/'
'''

class HardDrive(models.Model):
    creationDate = models.DateField(db_column='Creation Date', blank=True, null=True)
    serialNo = models.CharField(db_column='Serial Number', max_length=10, primary_key=True, unique=True)
    manufacturer = models.CharField(db_column='Manufacturer', max_length=50, choices=MANUFACTURER_CHOICES, blank=True, null=True)
    modelNo = models.CharField(db_column='Model Number', max_length=10, blank=True, null=True)
    hdType = models.CharField(db_column=' Hard Drive Type', max_length=50, choices=HD_TYPE_CHOICES)
    connPort = models.CharField(db_column=' Hard Drive Connection Port', max_length=50 ,choices=CONN_PORT_CHOICES)
    hdSize = models.CharField(db_column='Hard Drive Size', max_length=50, choices=HD_MEMORY_SIZES)
    hdClass = models.CharField(db_column=' Hard Drive Classification', max_length=50, choices=CLASS_CHOICES,  blank=True, null=True)
    justiClass = models.FileField(db_column='Justification for Classification Change',  blank=True, null=True, upload_to='Justification_Class_Change/')
    imageVerID = models.IntegerField(db_column='Image Version ID', blank=True, null=True)
    btStatus = models.BooleanField(db_column='Boot Test Passed?',  blank=True, null=True)
    btExpDate = models.DateField(db_column='Boot Expiration Date',  blank=True, null=True)
    hdStatus = models.CharField(db_column='HD Status', max_length=50, choices=HD_STATUS_CHOICES)
    justiStatus = models.FileField(db_column='Justification Change Status',  blank=True, null=True, upload_to='Justification_Status_Change/')
    issueDate = models.DateField(db_column='Issue Date',  blank=True, null=True)
    expectRetDate = models.DateField(db_column='Expected Returned Date',  blank=True, null=True)
    justiRetDate = models.FileField(db_column='Justification Change Return Date',  blank=True, null=True, upload_to='Justification_Return_Date/')
    actualRetDate = models.DateField(db_column='Actual Returned Date', blank=True, null=True)
    modDate = models.DateField(db_column='Modified Date', blank=True, null=True)    

    class Meta:
        managed = False
        db_table = 'harddrive'