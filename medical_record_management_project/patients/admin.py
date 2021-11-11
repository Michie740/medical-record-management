from django.contrib import admin
from patients import models


class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name']
    search_fields = ['patient_id', 'first_name', 'last_name']


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_id', 'street_address', 'city', 'zip_code', 'state'
    ]
    search_fields = [
        'address_id', 'street_address', 'city', 'zip_code', 'state'
    ]


admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Address, AddressAdmin)
