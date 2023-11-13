from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField

# Create your models here.
class BusinessProfileCategory(models.Model):
    category = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class BusinessProfile(models.Model):
    # Set their name, description, email, contact_number, category, owner, operating_hours, logo, cover_photo, website, social_medialinks and location.    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True)
    category = models.ForeignKey(BusinessProfileCategory, on_delete=models.SET_NULL, null=True)
    weekdays_starting_hour = models.TimeField(blank=True, null=True)
    weekdays_ending_hour = models.TimeField(blank=True, null=True)
    weekends_starting_hour = models.TimeField(blank=True, null=True)
    weekends_ending_hour = models.TimeField(blank=True, null=True)
    logo = models.FileField(upload_to="business_profile_logos/")
    cover_photo = models.FileField(upload_to="business_profile_logos/")
    website = models.URLField(blank=True, null=True)
    x = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    stackoverflow = models.URLField(blank=True, null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

