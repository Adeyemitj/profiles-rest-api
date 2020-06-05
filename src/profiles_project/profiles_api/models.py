from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""
    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""
        if not email: #check for email input
            raise ValueError('Users must have an email address')

        #normalizes email address
        email = self.normalize_email(email)
        #create a new user profile objects
        user = self.model(email=email, name=name)
        #set user's password
        user.set_password(password)
        #save to db
        user.save(using=self._db)

        return user

    #function to create a new superuser
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        #assign variables to user
        user.is_superuser = True
        user.is_staff = True

        #save to db
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a "a user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' # making email a default username
    REQUIRED_FIELDS = ['name']

    #function to get a user's full name
    def get_full_name(self):

        return self.name

    #function to get a user's short name
    def get_short_name(self):

        return self.name

    #return string objects
    def __str__(self):

        return self.email
