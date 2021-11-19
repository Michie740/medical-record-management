from django.test import TestCase
from django.urls import reverse
from users.tests import factories as user_factories
from users import models as user_models


class TestCustomSignupForm(TestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('account_signup')
        self.test_user = user_factories.UserFactory()

    def test_signup_url(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_non_unique_username(self):
        duplicated_data = {
            'username': self.test_user.username,
            'first_name': "TestFirstName",
            'last_name': "TestLastName",
            'password1': 'TestPassword123',
            'password2': 'TestPassword123',
            'email': "test_user_duplicate@example.com",
            'security_level': user_models.User.MEDIUM_LEVEL_CLINICIAN,
            'security_q1': "q1",
            'security_q2': "q2",
            'security_q3': "q3",
            'security_a1': "a1",
            'security_a2': "a2",
            'security_a3': "a3",
        }
        response = self.client.post(self.url, data=duplicated_data)
        self.assertContains(
            response,
            "A user with that username already exists."
        )

    def test_correct(self):
        correct_data = {
            'username': "test_correct_username",
            'first_name': "TestFirstName",
            'last_name': "TestLastName",
            'password1': 'TestPassword123',
            'password2': 'TestPassword123',
            'email': "test_user_duplicate@example.com",
            'security_level': user_models.User.MEDIUM_LEVEL_CLINICIAN,
            'security_q1': "q1",
            'security_q2': "q2",
            'security_q3': "q3",
            'security_a1': "a1",
            'security_a2': "a2",
            'security_a3': "a3",
        }
        users_pre_count = user_models.User.objects.count()

        response = self.client.post(self.url, data=correct_data)
        users_post_count = user_models.User.objects.count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(users_pre_count+1, users_post_count)
        self.assertEqual('/accounts/confirm-email/', response['location'])
