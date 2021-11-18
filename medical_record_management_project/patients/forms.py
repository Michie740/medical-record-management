from django.forms import ModelForm, formset_factory
from patients import models as patient_models


class AddressForm(ModelForm):
    class Meta:
        model = patient_models.Address
        fields = ['street_address', 'city', 'zip_code', 'state']


AddressFormSet = formset_factory(AddressForm, extra=1, can_delete=False)


class PatientForm(ModelForm):
    class Meta:
        model = patient_models.Patient
        fields = ['first_name', 'last_name', 'dob',
                  'preexisting_conditions', 'allergies', 'height_ft',
                  'height_in', 'weight', 'email', 'phone']
