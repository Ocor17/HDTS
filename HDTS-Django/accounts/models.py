from operator import is_
from djongo import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

'''
The User Class has all the basic attributes the Django has included 
    The Object is stored in the 'users' collection on our Mongo database
    The Django Attributes are the following:
        -id
        -password
        -last_login
        -is_superuser
        -username
        -first_name
        -last_name
        -email
        -is_staff
        -is_active
        -date_joined
'''
class User(models.Model):
    
 

    class Meta:
        managed = False
        db_table = 'users'


