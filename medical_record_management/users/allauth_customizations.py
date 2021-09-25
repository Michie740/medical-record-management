from allauth.account import forms as allauth_forms
from allauth.utils import set_form_field_order
from users.forms import UserCreateForm


class CustomSignupForm(UserCreateForm, allauth_forms.SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_order = [
            'username', 'password', 'first_name', 'last_name', 'email',
            'security_level', 'security_q1', 'security_a1',
            'security_q2', 'security_a2', 'security_q3', 'security_a3'
        ]
        set_form_field_order(self, field_order)
