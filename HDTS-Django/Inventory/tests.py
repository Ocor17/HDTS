
from django.test import TestCase
from .forms import *
from .models import HardDrive
import datetime

class InventoryTestCase(TestCase):


    def setUp(self):
        form = addNewHardDrive(
            serialNo =  1234, hdType = 'ssd', connPort = 'sata',
            hdSize = '500gb', hdStatus = 'assigned', actualRetDate = datetime.date.today,
            modDate = datetime.date.today
        )
        form.save()
        form = addNewHardDrive(
            serialNo =  2345, hdType = 'ssd', connPort = 'sata',
            hdSize = '500gb', hdStatus = 'assigned', actualRetDate = datetime.date.today,
            modDate = datetime.date.today
        )
        form.save()
        form = addNewHardDrive(
            serialNo =  3456, hdType = 'ssd', connPort = 'sata',
            hdSize = '500gb', hdStatus = 'assigned', actualRetDate = datetime.date.today,
            modDate = datetime.date.today
        )
        form.save()
        
    def test_form_date_is_today(self):
        hd = HardDrive.objects.get(serialNo= 1234)
        self.assertEquals(hd.creationDate, datetime.date.today)

    def test_form_is_unique(self):
        set = HardDrive.objects.filter(serialNo=1234)
        self.assertEquals(set.count, 1)

    