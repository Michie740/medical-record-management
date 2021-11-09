from django.forms import ModelForm
from patients import models as patient_models


class PatientForm(ModelForm):
    class Meta:
        model = patient_models.Patient
        fields = ['address', 'first_name', 'last_name', 'dob', 'preexisting_conditions', 'allergies', 'height_ft', 'height_in', 'weight', 'email', 'phone']
        
class AddressForm(ModelForm):
    class Meta:
        model = patient_models.Address
        fields = ['street_address', 'city', 'zip_code', 'state']
