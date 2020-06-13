from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""
    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""
        #check for email input
        if not email:
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
    """Represent "a user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # making email a default username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    #helper function to get a user's full name
    def get_full_name(self):

        return self.name

    #helper function to get a user's short name
    def get_short_name(self):

        return self.name

    #helper return string objects
    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email

# Profile to store all profiles update
class ProfileFeedItem(models.Model):
    """Profiles status update."""
    # add fields that point to user's profile that correspond to update.
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
