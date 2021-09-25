from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users import models as user_models
from users.allauth_customizations import CustomSignupForm

from allauth.account import views as allauth_views
from allauth.account.views import LoginView, PasswordChangeView


class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user_models.LoginRecord.objects.create(user=form.user)
        return response


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('')


class CustomSignupView(allauth_views.SignupView):
    form_class = CustomSignupForm
