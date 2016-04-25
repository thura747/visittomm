from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.utils import timezone
from tinymce.models import HTMLField

from ckeditor.fields import RichTextField

from ckeditor.widgets import CKEditorWidget

# class Agencies(User):
#     def __unicode__(self):
#          return self.last_name + self.first_name
#
#     user = models.OneToOneField(User)
#
#     name = models.CharField(max_length=200)
#     phone = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     emails = models.CharField(max_length=200, null=True)
#     website = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ('name',)

class RegionsStates(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Cities(models.Model):
    name = models.CharField(max_length=200)
    city_code = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    # description = models.TextField()
    # content = HTMLField()
    content = RichTextField(null=True)

    lat = models.CharField(max_length=20, null=True)
    lon = models.CharField(max_length=20, null=True)

    i_airport = models.BooleanField(default=False)     # International airports
    d_airport = models.BooleanField(default=False)     # Domestic airports
    bus = models.BooleanField(default=False)
    cruise = models.BooleanField(default=False)
    car = models.BooleanField(default=False)
    city = models.BooleanField(default=False)   # city of Region or State
    publish = models.BooleanField(default=False)

    region_id = models.ForeignKey(RegionsStates, null=True, related_name='cities_region_id')

    def __str__(self):
        return self.name


class Destinations(models.Model):
    name = models.CharField(max_length=200)
    content = RichTextField(null=True)

    lat = models.CharField(max_length=20, null=True)
    lon = models.CharField(max_length=20, null=True)

    i_airport = models.BooleanField(default=False)     # International airports
    d_airport = models.BooleanField(default=False)     # Domestic airports
    train = models.BooleanField(default=False)
    bus = models.BooleanField(default=False)
    cruise = models.BooleanField(default=False)
    car = models.BooleanField(default=False)
    city = models.BooleanField(default=False)   # city of Region or State
    publish = models.BooleanField(default=False)

    region_id = models.ForeignKey(RegionsStates, null=True, related_name='destination_region_id')
    city_id = models.ForeignKey(Cities, null=True, related_name='destination_city_id')

    def __str__(self):
        return self.name


class Companies(models.Model):
    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    emails = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=200, null=True)
    caution = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    created_by = models.ForeignKey('auth.User', null=True, related_name='company_created_by')
    updated_by = models.ForeignKey('auth.User', null=True, related_name='company_updated_by')
    user_ids = models.ManyToManyField('auth.User', related_name='user_ids')
    # agent_ids = models.ManyToManyField(Agencies)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Packages(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    description = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    created_by = models.ForeignKey('auth.User', null=True, related_name='packages_created_by')
    updated_by = models.ForeignKey('auth.User', null=True, related_name='packages_updated_by')

    company_id = models.ForeignKey(Companies, related_name='company_id')

    origin = models.ForeignKey(Cities, null=True, related_name='package_origin_city_id')
    destination = models.ForeignKey(Cities, null=True, related_name='package_destination_city_id')

    def __str__(self):
        return self.title


class Routes(models.Model):
    route_code = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)

    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE, null=True, related_name='package_id')

    def __str__(self):
        return self.location


class Headers(models.Model):
    title = models.CharField(max_length=200)
    caption = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Images(models.Model):
    title = models.CharField(max_length=200)
    path = models.CharField(max_length=200)

    header_id = models.ForeignKey(Headers, on_delete=models.CASCADE, null=True, related_name='header_id')
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True, related_name='images_city_id')














class Post2(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# need to use future. inherit user model
#
# from django.db import models
# from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
#
#
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=MyUserManager.normalize_email(email),
#             date_of_birth=date_of_birth,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, date_of_birth, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         u = self.create_user(username,
#                              password=password,
#                              date_of_birth=date_of_birth
#                              )
#         u.is_admin = True
#         u.save(using=self._db)
#         return u
#
#
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth']
#
#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def __unicode__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin