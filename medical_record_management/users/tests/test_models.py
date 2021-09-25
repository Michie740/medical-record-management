from django.test import TestCase

from users import models as user_models
from users.tests import factories as user_factories


class TestUser(TestCase):
    def setUp(self):
        super().setUp()
        self.user = user_factories.UserFactory()

    def test_str_method(self):
        expected = ("Username is test_username, "
                    "full name is TestFirstName TestLastName and "
                    "security level is {}".format(
                        user_models.User.HIGH_LEVEL_CLINICIAN)
                    )
        actual = str(self.user)

        self.assertEqual(expected, actual)
