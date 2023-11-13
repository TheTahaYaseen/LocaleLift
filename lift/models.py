from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

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
    operating_hours = models.JSONField(blank=True, null=True)
    logo = models.FileField(upload_to="business_profile_logos/")
    cover_photo = models.FileField(upload_to="business_profile_logos/")
    website = models.URLField(blank=True, null=True)
    social_media = models.JSONField(blank=True, null=True)
    location_lattiude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

