from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from users.views import MediumOrHighSecurityLevelOnlyMixin
from records import models as record_models
from patients import models as patient_models


class RecordListView(MediumOrHighSecurityLevelOnlyMixin, ListView):
    model = record_models.Record

    template_name = "records/record_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['patient'] = patient_models.Patient.objects.get(
            pk=self.get_patient_pk()
        )
        return context

    def get_patient_pk(self):
        return self.kwargs.get('pk')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(patient=self.get_patient_pk())
        return queryset


class RecordAddView(MediumOrHighSecurityLevelOnlyMixin, CreateView):
    model = record_models.Record

    fields = ['notes', 'attachments']

    def get_patient_pk(self):
        return self.kwargs.get('pk')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['patient'] = patient_models.Patient.objects.get(
            pk=self.get_patient_pk()
        )
        return context

    def get_success_url(self):
        return reverse_lazy('patient_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.patient = patient_models.Patient.objects.get(
            pk=self.get_patient_pk()
        )
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print("Record Add Errors:", form.errors)
        return super().form_invalid(form)
