from django import forms

from .models import BusinessProfile

class BusinessProfileForm(forms.ModelForm):
    
    class Meta:
        model = BusinessProfile
        fields = "__all__"
        exclude = ["category"]