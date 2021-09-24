from django import forms

from users import models as user_models


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = user_models.User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'security_level',
                  'security_q1', 'security_a1',
                  'security_q2', 'security_a2',
                  'security_q3', 'security_a3']
        widgets = {
            "password": forms.PasswordInput(),
        }
