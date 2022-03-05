from djongo import models

# Create your models here.

class User(models.Model):
    
 

    class Meta:
        managed = False
        db_table = 'users'