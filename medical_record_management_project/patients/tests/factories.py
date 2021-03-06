import factory.fuzzy
import datetime
import pytz
from patients import models as patient_models
from users.tests import factories as user_factories


class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = patient_models.Patient

    doctor = factory.SubFactory(user_factories.UserFactory)
    first_name = "test"
    last_name = "patient"
    dob = pytz.utc.localize(datetime.datetime(2000, 10, 3))
    preexisting_conditions = "none"
    allergies = "nuts"
    height_ft = 5
    height_in = 5
    weight = 140
    email = "test@example.com"
    phone = "5017891825"


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = patient_models.Address

    address_id = factory.Sequence(lambda n: "%d" % n)
    street_address = factory.Sequence(lambda n: "123%d Main St" % n)
    city = "Brooklyn"
    zip_code = "12345"
    state = "NY"
