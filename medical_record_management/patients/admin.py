from django.contrib import admin
from patients import models


class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name']
    search_fields = ['patient_id', 'first_name', 'last_name']


admin.site.register(models.Patient)
