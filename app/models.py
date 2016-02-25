from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Device(models.Model):
    device_id = models.CharField(max_length=255, default="")
    device_name = models.CharField(max_length=40, default="")
    time_created = models.DateTimeField(auto_now_add=True)
    vehicle_id = models.CharField(max_length=255, blank=True, null=True)
    time_driven = models.BigIntegerField(default=0)
    distance_driven = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    location_address = models.CharField(max_length=255, default="")
    location_lat = models.FloatField(blank=True, null=True)
    location_lng = models.FloatField(blank=True, null=True)

class Trip(models.Model):
    trip_id = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=20, default="in_progress")
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=255, default="")
    vehicle_id = models.CharField(max_length=255, default="")
    distance = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    duration = models.BigIntegerField(default=0)
    current_speed = models.FloatField(default=0.00)
    average_moving_speed = models.FloatField(default=0.00)
    average_speed = models.FloatField(default=0.00)
    max_speed = models.IntegerField(default=0)
    hard_accel_count = models.IntegerField(default=0)
    hard_brake_count = models.IntegerField(default=0)
    stop_count = models.IntegerField(default=0)
    start_address = models.CharField(max_length=255, default="")
    end_address = models.CharField(max_length=255, default="")
    start_lat = models.FloatField(blank=True, null=True)
    start_lng = models.FloatField(blank=True, null=True)
    stop_lat = models.FloatField(blank=True, null=True)
    stop_lng = models.FloatField(blank=True, null=True)

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=255, default="")
    device_id = models.CharField(max_length=255, default="")
    year = models.IntegerField(default=-1)
    make = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=100, default="")
    trim = models.CharField(max_length=50, default="")


class VindigoUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class VindigoUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = VindigoUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
