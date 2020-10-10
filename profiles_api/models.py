from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a user profile inside our system
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # required when substituting the custom user model in django
    is_staff = models.BooleanField(default=False)

    object = user_profile_manager()  # object manager required

    USERNAME_FIELD = 'email'  # user to use email instead of username to sign in
    REQUIRED_FIELDS = ['name']

    # helper functions
    def get_full_name(self):
        """Used to get a users full name"""
        return self.name

    def get_short_name(self):
        """Used to get the users short name"""
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.email
