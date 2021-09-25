from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SUPERUSER = 1
    ADMIN = 2
    BASIC = 3
    HIGH_LEVEL_CLINICIAN = 4
    MEDIUM_LEVEL_CLINICIAN = 5
    LOW_LEVEL_CLINICIAN = 6
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
