import uuid
from django.core.exceptions import ValidationError
from django.db import models
from users import models as user_models
from phone_field import PhoneField


class Patient(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateTimeField()
    preexisting_conditions = models.CharField(max_length=700)
    allergies = models.CharField(max_length=700)
    height_ft = models.PositiveIntegerField()
    height_in = models.PositiveIntegerField()
    weight = models.FloatField()
    email = models.CharField(max_length=200)
    phone = PhoneField(help_text="Patient's preferred phone number")

    def save(self):
        if (self.doctor.security_level != user_models.User.HIGH_LEVEL_CLINICIAN) and (self.doctor.security_level != user_models.User.MEDIUM_LEVEL_CLINICIAN):
            return ValidationError("Doctor must be a medium or high level clinician")
        else:
            super().save()

    def __str__(self):
        return "Patient ID is {} and name is {}".format(self.patient_id, self.first_name, self.last_name)