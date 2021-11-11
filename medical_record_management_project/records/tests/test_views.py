from django.test import Client, TestCase
from django.urls import reverse
from patients.tests import factories as patient_factories
from users.tests import factories as user_factories
from records.tests import factories as record_factories


class TestRecordListView(TestCase):

    def setUp(self):
        super().setUp()
        self.doctor = user_factories.UserFactory()
        # log in as doctor
        self.client = Client()
        self.client.force_login(self.doctor)

        self.patient = patient_factories.PatientFactory()
        self.patient.doctor = self.doctor

        self.url = reverse("list_records", kwargs={'pk': self.patient.pk})

    def test_get_no_records(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, "List of Records for {} {}".format(
            self.patient.first_name, self.patient.last_name))
        self.assertContains(response, "<td>No records.</td>")

    def test_get_records(self):
        record = record_factories.RecordFactory()
        record.patient = self.patient
        record.save()

        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, "List of Records for {} {}".format(
            self.patient.first_name, self.patient.last_name))
        self.assertNotContains(response, "<td>No records.</td>")
        self.assertContains(response, record.notes)
        self.assertContains(response, record.attachments)
