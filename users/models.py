from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

class UserModuleManager(BaseUserManager):
    use_in_migrations = True 

    def _create_user(self, phone, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            raise ValueError('The phone number must be set')
        
        # email = self.normalize_email(email)
        # user = self.model(email=email, **extra_fields)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)  # Properly set the password
        user.save(using=self._db)  # Ensure the correct database is used
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)        
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'user_management'        

    phone = models.CharField(max_length=20, blank=False, null=False, unique=True)

    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)    
    date_activated = models.DateTimeField(auto_now_add=True)    
    town = models.CharField(max_length=100, blank=True, null=True)    
    gender = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateTimeField(auto_now=False, null=True) 
    email = models.EmailField(max_length=255, blank=True, null=True)   
    address = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    identification_document = models.CharField(max_length=255, blank=True, null=True)
    identification_document_number = models.CharField(max_length=255, blank=True, null=True)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserModuleManager()