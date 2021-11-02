from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users import models as user_models
from users.forms import CustomSignupForm

from allauth.account import views as allauth_views
from allauth.account.views import LoginView, PasswordChangeView


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy('patient_list')


class CustomSignupView(allauth_views.SignupView):
    success_url = reverse_lazy('patient_list')
    model = user_models.User
    form_class = CustomSignupForm
    template_name = 'users/signup.html'


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('patient_list')


class MediumOrHighSecurityLevelOnlyMixin(
        UserPassesTestMixin, LoginRequiredMixin):

    def test_func(self):
        return (
                (not self.request.user.is_anonymous)
                and self.request.user.is_medium_or_high_clinician
        )
