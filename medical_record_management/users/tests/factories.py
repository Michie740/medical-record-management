import factory.fuzzy

from users import models as user_models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = user_models.User

    username = factory.Sequence(lambda n: "user_name_%d" % n)
    password = "test_password123"
    first_name = "TestFirstName"
    last_name = "TestLastName"
    email = "test_email@example.com"
    security_level = user_models.User.HIGH_LEVEL_CLINICIAN
    security_q1 = "favorite color?"
    security_q2 = "favorite food?"
    security_q3 = "favorite animal?"
    security_a1 = "test_color"
    security_a2 = "test_food"
    security_a3 = "test_animal"
