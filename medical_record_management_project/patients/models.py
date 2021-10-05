import uuid
from django.core.exceptions import ValidationError
from django.db import models
from users import models as user_models
from phone_field import PhoneField


class Address(models.Model):
    address_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,
        editable=False
    )
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return "{} \n{}, {} {}".format(
            self.street_address, self.city, self.state, self.zip_code)


"""
A thought:

Doctors should not cascade on delete to patients.
Patients should be kept in the system so that their information
can be transferred or they can be reassigned to a new doctor.

-rsk
"""


class Patient(models.Model):
    patient_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,
        editable=False, unique=True
    )
    doctor = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE
    )
    address = models.ForeignKey(
        Address, null=True, on_delete=models.SET_NULL
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateTimeField()
    preexisting_conditions = models.CharField(max_length=700)
    allergies = models.CharField(max_length=700)
    height_ft = models.PositiveIntegerField()
    height_in = models.PositiveIntegerField()
    weight = models.FloatField()
    email = models.CharField(max_length=200)
    phone = PhoneField(
        help_text="Patient's preferred phone number"
    )

    def save(
            self, force_insert=False, force_update=False,
            using=None, update_fields=None):
        if (self.doctor.security_level not in [
            user_models.User.HIGH_LEVEL_CLINICIAN,
            user_models.User.MEDIUM_LEVEL_CLINICIAN
        ]):
            return ValidationError(
                "Doctor must be a medium or high level clinician"
            )
        else:
            super().save()

    def __str__(self):
        return "Patient ID is {} and name is {} {}".format(
            self.patient_id, self.first_name, self.last_name)


class Records(models.Model):
    record_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,
        editable=False
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE
    )
    notes = models.CharField(max_length=700)
    attachments = models.CharField(max_length=700)

    def __str__(self):
        return "{} \n\n{}".format(
            self.notes, self.attachments)
