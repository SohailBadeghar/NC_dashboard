from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class BaseModel(models.Model):
    """
    Abstract base model with common fields for other models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Set a default value

    class Meta:
        abstract = True


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    Model to store user details, extending AbstractBaseUser and PermissionsMixin.
    """
    emp_id = models.CharField(max_length=10, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    has_resigned = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # for admin access
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['emp_id']

    def __str__(self):
        return self.email
