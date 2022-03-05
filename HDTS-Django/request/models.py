from django.db import models

# Create your models here.
class RequestList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Request(models.Model):
    todoList = models.ForeignKey(RequestList, on_delete=models.CASCADE, related_name="requestlist", null=True)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text