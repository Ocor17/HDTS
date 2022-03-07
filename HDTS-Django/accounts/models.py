from operator import is_
from djongo import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(models.Model):
    
 

    class Meta:
        managed = False
        db_table = 'users'


