from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SUPERUSER = 'Superuser'
    ADMIN = 'Admin'
    BASIC = 'Basic'
    HIGH_LEVEL_CLINICIAN = 'High_level_clinician'
    MEDIUM_LEVEL_CLINICIAN = 'Medium_level_clinician'
    LOW_LEVEL_CLINICIAN = 'Low_level_clinician'
    SECURITY_LEVELS = (
        (SUPERUSER, 'Superuser'),
        (ADMIN, 'Admin'),
        (BASIC, 'Basic'),
        (HIGH_LEVEL_CLINICIAN, 'High level clinician'),
        (MEDIUM_LEVEL_CLINICIAN, 'Medium level clinician'),
        (LOW_LEVEL_CLINICIAN, 'Low level clinician'),
    )
    security_level = models.CharField(
        choices=SECURITY_LEVELS, max_length=50, default=BASIC
    )
    # TODO: ADD A CONSTANT FOR THE 200
    security_q1 = models.CharField(max_length=200)
    security_q2 = models.CharField(max_length=200)
    security_q3 = models.CharField(max_length=200)
    security_a1 = models.CharField(max_length=200)
    security_a2 = models.CharField(max_length=200)
    security_a3 = models.CharField(max_length=200)

    def __str__(self):
        return (
            "Username is {}, full name is {} {}"
            " and security level is {}".format(
                self.username, self.first_name,
                self.last_name, self.security_level
            )
        )

    @property
    def is_medium_or_high_clinician(self):
        is_medium_level = (self.security_level == User.MEDIUM_LEVEL_CLINICIAN)
        is_high_level = (self.security_level == User.HIGH_LEVEL_CLINICIAN)
        return is_high_level or is_medium_level
