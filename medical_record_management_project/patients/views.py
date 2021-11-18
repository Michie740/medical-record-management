from users.views import MediumOrHighSecurityLevelOnlyMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from patients import models as patient_models
from patients import forms as patient_forms


class PatientListView(MediumOrHighSecurityLevelOnlyMixin, ListView):
    model = patient_models.Patient

    template_name = "patients/patient_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(doctor=self.request.user)
        return queryset


class PatientAddView(CreateView):
    model = patient_models.Patient

    fields = ['first_name', 'last_name',
              'dob', 'preexisting_conditions', 'allergies',
              'height_ft', 'height_in', 'weight', 'email', 'phone']

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["formset"] = patient_forms.AddressFormSet
        return context_data

    def get_success_url(self):
        return reverse_lazy('patient_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.doctor = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class PatientEditView(UpdateView):
    model = patient_models.Patient

    template_name_suffix = '_update_form'

    fields = ['doctor', 'address', 'first_name', 'last_name',
              'dob', 'preexisting_conditions', 'allergies',
              'height_ft', 'height_in', 'weight', 'email', 'phone']

    def get_success_url(self):
        return '<pk>'


class AddressAddView(CreateView):
    model = patient_models.Address

    fields = ['street_address', 'city', 'zip_code', 'state']

    def get_success_url(self):
        return ''
