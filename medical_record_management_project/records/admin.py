from django.contrib import admin
from records import models


class RecordsAdmin(admin.ModelAdmin):
    list_display = ['record_id', 'patient', 'notes', 'attachments']
    search_fields = ['record_id', 'patient', 'notes', 'attachments']


admin.site.register(models.Record, RecordsAdmin)
