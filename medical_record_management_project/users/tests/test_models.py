from django.test import TestCase

from users import models as user_models
from users.tests import factories as user_factories


class TestUser(TestCase):
    def setUp(self):
        super().setUp()
        self.user = user_factories.UserFactory()

    def test_str_method(self):
        expected = ("Username is {}, "
                    "full name is {} {} and "
                    "security level is {}".format(
                        self.user.username,
                        self.user.first_name,
                        self.user.last_name,
                        user_models.User.HIGH_LEVEL_CLINICIAN)
                    )
        actual = str(self.user)

        self.assertEqual(expected, actual)
