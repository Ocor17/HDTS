from ast import Try
from django.utils import timezone
from operator import is_
from djongo import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from datetime import date

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

class AccountManager(BaseUserManager):
    
    
    def create_superuser(self,email,username,first_name,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must have staff assigned to True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must havbe')
        
        return self.create_user(email,username,first_name,password, **other_fields)


    
    def create_user(self,email,username,first_name,password, **other_fields):
        
        if not email:
            raise ValueError(_("Email must be provided"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, 
                        first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True,primary_key=True)
    username = models.CharField(max_length=30)
    user_role = models.CharField(max_length=100)
    direct_supervisor_email = models.EmailField(max_length=30)
    branch_chief_name = models.CharField(max_length=30)
    account_status = models.CharField(max_length=30,default="Pending")
    last_modified = models.DateField(default=timezone.now())
    
    #needed for superuser functionality
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name']
    
    def __str__(self):
        return self.email

 

    class Meta:
        managed = False
        db_table = 'users'


