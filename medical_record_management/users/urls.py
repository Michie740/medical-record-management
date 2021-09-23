from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="users/home.html"), name='home'),
    path('sign_up/', views.UserCreateView.as_view(), name='sign_up'),
]