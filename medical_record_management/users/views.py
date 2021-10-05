from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users import models as user_models
from users.forms import CustomSignupForm

from allauth.account import views as allauth_views
from allauth.account.views import LoginView, PasswordChangeView


class CustomLoginView(LoginView):
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        user_models.LoginRecord.objects.create(user=form.user)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class CustomSignupView(allauth_views.SignupView):
    model = user_models.User
    form_class = CustomSignupForm
    template_name = 'users/signup.html'


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('patient_list')


class MediumOrHighSecurityLevelOnlyMixin(UserPassesTestMixin, LoginRequiredMixin):

    def test_func(self):
        return (not self.request.user.is_anonymous) and self.request.user.is_medium_or_high_clinician
