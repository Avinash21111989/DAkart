from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,username,first_name,last_name,phone_number,email,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username address")
        
        User = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number
           
        )

        User.set_password(password)
        User.save(using=self.db)
        return User
    
    def create_superuser(self,first_name,last_name,username,email,password,phone_number):
        User = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            password = password,
            last_name = last_name,
            phone_number = phone_number
        )

        User.is_admin = True
        User.is_active = True
        User.is_staff = True
        User.is_superadmin = True
        User.save(using=self.db)
        return User





class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone_number = models.CharField(max_length=10,unique=True)
    date_joined = models.DateField(auto_now_add=True)
    last_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','phone_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True
