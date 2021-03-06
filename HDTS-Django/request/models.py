from djongo import models
from accounts.models import User

# Create your models here.
class RequestList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requestlist", null=True)
    eventName = models.CharField(max_length=200)
    # info from form
    classification = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    port = models.CharField(max_length=200, null=True)
    size = models.IntegerField(null=True)
    type = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True)
    eventDescription = models.CharField(max_length=200, null=True)
    eventLocation = models.CharField(max_length=200, null=True)
    eventType = models.CharField(max_length=200, null=True)
    reportingCycle = models.IntegerField(null=True)
    eventStatus = models.CharField(max_length=200, null=True)
    eventStartDate = models.DateField(max_length=200, null=True)
    eventEndDate = models.DateField(max_length=200, null=True)
    requestStatus = models.CharField(max_length=200, null=True)

    request_number = models.IntegerField(null=False)
    ticket_number = models.CharField(max_length=20, null=False)
    request_creation_date = models.DateTimeField(max_length=200)
    hd_pick_up_date = models.DateField(max_length=200)
    hd_return_date = models.DateField(max_length=200)

    class Meta:
        managed = False
        db_table = 'requestlist'
