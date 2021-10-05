from django.test import TestCase
from mock import MagicMock
from django.contrib.auth.models import AnonymousUser
from users.tests import factories as user_factories
from users import views as user_views
from users import models as user_models


class TestMediumOrHighSecurityLevelOnlyMixin(TestCase):
    def setUp(self):
        super().setUp()
        self.mixin = user_views.MediumOrHighSecurityLevelOnlyMixin()

    def test_test_func_not_qualified_clinician(self):
        user = user_factories.UserFactory(security_level=user_models.User.BASIC)
        self.mixin.request = MagicMock(user=user)

        result = self.mixin.test_func()

        self.assertFalse(result)

    def test_test_func_high_level_clinician(self):
        high_level_user = user_factories.UserFactory(security_level=user_models.User.HIGH_LEVEL_CLINICIAN)
        self.mixin.request = MagicMock(user=high_level_user)

        result = self.mixin.test_func()

        self.assertTrue(result)

    def test_test_func_qualified_clinician(self):
        med_level_user = user_factories.UserFactory(security_level=user_models.User.MEDIUM_LEVEL_CLINICIAN)
        self.mixin.request = MagicMock(user=med_level_user)

        result = self.mixin.test_func()

        self.assertTrue(result)

    def test_test_func_not_logged_in(self):
        self.mixin.request = MagicMock(user=AnonymousUser())
        result = self.mixin.test_func()

        self.assertFalse(result)
