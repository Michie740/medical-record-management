from django.test import TestCase

from patients.tests import factories as patient_factories


class TestPatient(TestCase):
    def setUp(self):
        super().setUp()
        self.patient = patient_factories.PatientFactory()

    def test_str_method(self):
        expected = ("Patient ID is {} and name is {} {}".format(
            self.patient.patient_id, self.patient.first_name, self.patient.last_name)
        )
        actual = str(self.patient)

        self.assertEqual(expected, actual)
