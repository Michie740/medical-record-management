from django.test import Client, TestCase

from django.urls import reverse
from patients.tests import factories as patient_factories
from patients import models as patient_models
from users.tests import factories as user_factories
from users import models as user_models


class TestPatientListView(TestCase):

    def setUp(self):
        super().setUp()
        self.doctor = user_factories.UserFactory()
        self.client = Client()
        self.client.force_login(self.doctor)

        self.url = reverse("patient_list")

    def test_not_logged_in(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)

    def test_logged_in_no_patients(self):
        response = self.client.get(self.url)

        self.assertContains(response, "<td>No patients.</td>")

    def test_logged_in_with_patient(self):
        patient = patient_factories.PatientFactory(doctor=self.doctor)

        response = self.client.get(self.url)

        self.assertContains(response, patient.first_name)
        self.assertContains(response, patient.last_name)

    def test_logged_in_low_level(self):
        self.client.logout()
        self.doctor = user_factories.UserFactory(
            security_level=user_models.User.LOW_LEVEL_CLINICIAN
        )
        self.client.force_login(self.doctor)

        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)


class TestPatientAddView(TestCase):

    def setUp(self):
        self.address = patient_factories.AddressFactory()
        self.doctor = user_factories.UserFactory()
        self.url = reverse("add_patient")

    def test_get(self):
        response = self.client.get(self.url)

        self.assertContains(response, "<h1>Add Patient</h1>")
        self.assertContains(response, 'for="id_address">Address')

    def test_invalid_post(self):
        data = {}
        num_of_patients_before = patient_models.Patient.objects.all().count()

        response = self.client.post(self.url, data=data, follow=False)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'This field is required', count=12)
        num_of_patients_after = patient_models.Patient.objects.all().count()
        self.assertEqual(num_of_patients_before, num_of_patients_after)

    def test_valid_post(self):
        data = {
            "doctor": self.doctor.id,
            "address": self.address.address_id,
            "first_name": "First_Name",
            "last_name": "Last_Name",
            "dob": "01/02/03",
            "preexisting_conditions": "None",
            "allergies": "None",
            "height_ft": 5,
            "height_in": 4,
            "weight": 3,
            "email": "tester@example.com",
            "phone_0": "+1234567890",
            "phone_1": "+1234567890"
        }
        num_of_patients_before = patient_models.Patient.objects.all().count()

        response = self.client.post(self.url, data=data, follow=False)
        self.assertEqual(302, response.status_code)

        num_of_patients_after = patient_models.Patient.objects.all().count()
        self.assertEqual(num_of_patients_before+1, num_of_patients_after)


class TestPatientEditView(TestCase):

    def setUp(self):
        self.address = patient_factories.AddressFactory()
        self.doctor = user_factories.UserFactory()
        self.patient = patient_factories.PatientFactory()

        self.url = reverse("edit_patient", kwargs={'pk': self.patient.pk})

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, "<h1>Edit Patient</h1>")
        first_name_input = '<input type="text" name="first_name" value="{}"'.format(
            self.patient.first_name)
        self.assertContains(response, first_name_input)

    def test_invalid_post(self):
        # there are 12 fields, and only one is filled
        data = {
            "doctor": self.doctor.id
        }

        response = self.client.post(self.url, data=data, follow=False)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'This field is required', count=11)

    def test_valid_post(self):
        # there are 12 fields, and only one is filled
        data = {
            "doctor": self.doctor.id,
            "address": self.address.address_id,
            "first_name": "First_Name",
            "last_name": "Last_Name",
            "dob": "01/02/03",
            "preexisting_conditions": "None",
            "allergies": "None",
            "height_ft": 2,
            "height_in": 1,
            "weight": 2,
            "email": "tester@example.com",
            "phone_0": "+1234567890",
            "phone_1": "+1234567890"
        }

        response = self.client.post(self.url, data=data, follow=False)

        self.assertEqual(302, response.status_code)

        this_patient = patient_models.Patient.objects.get(patient_id=self.patient.patient_id)

        self.assertEqual(self.doctor.id, this_patient.doctor.id)
        self.assertEqual(self.address.address_id, this_patient.address.address_id)
        self.assertEqual("tester@example.com", this_patient.email)
