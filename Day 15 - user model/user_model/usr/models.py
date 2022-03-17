import os
import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError('User must have email.')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email=None, password=None):
        if not email:
            raise ValueError('User must have email.')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None):
        if not email:
            raise ValueError('User must have email.')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    create_at = models.DateTimeField(
        verbose_name=_('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated Time'),
        auto_now=True
    )
    username = models.CharField(
        unique=True,
        verbose_name=_('Username'),
        max_length=128,
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email'),
        max_length=256,
    )
    email_verified = models.BooleanField(
        verbose_name=_('Email Verified'),
        default=False
    )
    staff = models.BooleanField(
        verbose_name=_('Staff'),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_('Admin'),
        default=False
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.staff

    def has_perm(self, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
