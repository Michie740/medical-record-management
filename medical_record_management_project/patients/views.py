from users.views import MediumOrHighSecurityLevelOnlyMixin
from django.views.generic import ListView
from patients import models as patient_models


class PatientListView(MediumOrHighSecurityLevelOnlyMixin, ListView):
    model = patient_models.Patient

    template_name = "patients/patient_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(doctor=self.request.user)
        return queryset
