from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,BaseUserManager
# Create your models here.





def upload_to(instance, filename):
    return 'profiles/{filename}'.format(filename=filename)


class UserManager(BaseUserManager):

    def create_user(self,username , email,password,**extra_fields):
        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)
        user = self.model(username=username , email=email , **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self ,username , email ,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be given is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be given is_superuser=True')
        return self.create_user(username, email,password,**extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    objects= UserManager()

    USERNAME_FIELD ="username"
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    GENDER_STATUS = (
        ('male', 'male'),
        ('female','female'),
    )
    first_name = models.CharField(max_length=100, null=True , blank=True)
    last_name = models.CharField(max_length=100 , null=True , blank=True) 
    gender = models.CharField(max_length=10 , choices=GENDER_STATUS , null=True , blank=True)     
    image = models.ImageField(default='profiles/image-default.png', upload_to=upload_to , null=True , blank=True)
    user = models.OneToOneField('account.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


