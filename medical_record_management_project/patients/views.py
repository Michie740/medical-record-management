from users.views import MediumOrHighSecurityLevelOnlyMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from patients import models as patient_models


class PatientListView(MediumOrHighSecurityLevelOnlyMixin, ListView):
    model = patient_models.Patient

    template_name = "patients/patient_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(doctor=self.request.user)
        return queryset


class PatientAddView(CreateView):
    model = patient_models.Patient

    fields = ['doctor', 'address', 'first_name', 'last_name', 'dob', 'preexisting_conditions', 'allergies', 'height_ft', 'height_in', 'weight', 'email', 'phone']
    
    def get_success_url(self):
        return ''


class PatientEditView(UpdateView):
    model = patient_models.Patient

    template_name_suffix = '_update_form'

    fields = ['doctor', 'address', 'first_name', 'last_name', 'dob', 'preexisting_conditions', 'allergies', 'height_ft', 'height_in', 'weight', 'email', 'phone']
    
    def get_success_url(self):
        return '<pk>'


class AddressAddView(CreateView):
    model = patient_models.Address
    
    fields = ['street_address', 'city', 'zip_code', 'state']
    
    def get_success_url(self):
        return ''
