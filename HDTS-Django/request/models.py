from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RequestList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requestlist", null=True)
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Request(models.Model):
    requestList = models.ForeignKey(RequestList, on_delete=models.CASCADE, related_name="requestlist", null=True)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text