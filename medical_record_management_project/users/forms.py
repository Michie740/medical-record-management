
from allauth.account.forms import SignupForm
from django import forms
from users import models as user_models


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    security_level = forms.ChoiceField(
        choices=user_models.User.SECURITY_LEVELS)
    security_q1 = forms.CharField(max_length=200)
    security_q2 = forms.CharField(max_length=200)
    security_q3 = forms.CharField(max_length=200)
    security_a1 = forms.CharField(max_length=200)
    security_a2 = forms.CharField(max_length=200)
    security_a3 = forms.CharField(max_length=200)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.security_q1 = self.cleaned_data['security_q1']
        user.security_a1 = self.cleaned_data['security_a1']
        user.security_q2 = self.cleaned_data['security_q2']
        user.security_a2 = self.cleaned_data['security_a2']
        user.security_q3 = self.cleaned_data['security_q3']
        user.security_a3 = self.cleaned_data['security_a3']
        user.security_level = self.cleaned_data['security_level']
        user.save()
        return user
