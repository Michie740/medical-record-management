import os
import factory.fuzzy
from django.conf import settings
from patients.tests import factories as patient_factories
from records import models as record_models
from django.core.files.uploadedfile import SimpleUploadedFile


TEST_ATTACHMENT_LOCATION = os.path.join(
    settings.BASE_DIR, 'records', 'tests', 'data', 'test_attachment.txt'
)
TEST_ATTACHMENT = open(TEST_ATTACHMENT_LOCATION, 'rb')


class RecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = record_models.Record

    patient = factory.SubFactory(patient_factories.PatientFactory)
    notes = "patient is doing a bit better now"
    attachments = SimpleUploadedFile(
        TEST_ATTACHMENT_LOCATION, TEST_ATTACHMENT.read()
    )
