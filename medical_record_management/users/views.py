from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from users import forms as user_forms
from users import models as user_models


class UserCreateView(CreateView):
    model = user_models.User
    form_class = user_forms.UserCreateForm

    def form_invalid(self, form):
        print("UserCreate form errors", form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())