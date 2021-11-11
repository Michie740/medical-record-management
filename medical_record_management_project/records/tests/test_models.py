from django.test import TestCase

from records.tests import factories as record_factories


class TestRecord(TestCase):
    def setUp(self):
        super().setUp()
        self.record = record_factories.RecordFactory()

    def test_str_method(self):
        expected = "{} \n\n{}".format(
            self.record.notes, self.record.attachments)

        actual = str(self.record)

        self.assertEqual(expected, actual)
