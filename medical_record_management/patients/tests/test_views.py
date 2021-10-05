from django.test import Client, TestCase

from django.urls import reverse
from patients.tests import factories as patient_factories
from users.tests import factories as user_factories


class TestPatientListView(TestCase):

    def setUp(self):
        super().setUp()
        self.doctor = user_factories.UserFactory()
        self.client = Client()
        self.client.force_login(self.doctor)

        self.url = reverse("patient_list")

    def test_logged_in_no_patients(self):
        response = self.client.get(self.url)

        self.assertContains(response, "<td>No patients.</td>")

    def test_not_logged_in(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)

    def test_logged_in_with_patient(self):
        patient = patient_factories.PatientFactory(doctor = self.doctor)

        response = self.client.get(self.url)

        self.assertContains(response, patient.first_name)
        self.assertContains(response, patient.last_name)
