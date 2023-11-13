from django import forms
from .models import BusinessProfile
from phonenumber_field.modelfields import PhoneNumberField
from location_field.forms.plain import PlainLocationField
from location_field.widgets import LocationWidget

class BusinessProfileForm(forms.ModelForm):
    phone_number = PhoneNumberField()
    location = PlainLocationField(based_fields=[], widget=LocationWidget(attrs={'class': 'map-input'}))

    class Meta:
        model = BusinessProfile
        fields = "__all__"
        exclude = ["category"]
        widgets = {
            'phone_number': PhoneNumberField(attrs={'type': 'tel'}),
            'website': forms.URLInput(attrs={'type': 'url'}),
            'x': forms.URLInput(attrs={'type': 'url'}),
            'youtube': forms.URLInput(attrs={'type': 'url'}),
            'facebook': forms.URLInput(attrs={'type': 'url'}),
            'instagram': forms.URLInput(attrs={'type': 'url'}),
            'github': forms.URLInput(attrs={'type': 'url'}),
            'stackoverflow': forms.URLInput(attrs={'type': 'url'}),
            'weekdays_starting_hour': forms.TimeInput(attrs={'type': 'time'}),
            'weekdays_ending_hour': forms.TimeInput(attrs={'type': 'time'}),
            'weekends_starting_hour': forms.TimeInput(attrs={'type': 'time'}),
            'weekends_ending_hour': forms.TimeInput(attrs={'type': 'time'}),
        }
