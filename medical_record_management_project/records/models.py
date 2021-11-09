from django.db import models
from patients.models import Patient


class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE
    )
    notes = models.CharField(max_length=700)
    attachments = models.FileField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} \n\n{}".format(
            self.notes, self.attachments)
