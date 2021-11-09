from django.forms import ModelForm
from records import models as records_models


class RecordsForm(ModelForm):
    class Meta:
        model = records_models.Record
        fields = ['notes', 'attachments']
