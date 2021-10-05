from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from users import views as user_views

urlpatterns = [
    path('', TemplateView.as_view(
        template_name="users/home.html"
    ), name='home'),
    path('accounts/login/',
         user_views.CustomLoginView.as_view(),
         name="account_login"
         ),
    path('accounts/signup/', user_views.CustomSignupView.as_view(), name="account_signup"),
    path('accounts/password/change/',
         user_views.CustomPasswordChangeView.as_view(),
         name='account_change_password'),
    path('accounts/', include('allauth.urls')),
    path('', RedirectView.as_view(url='login/handle/', permanent=False)),
]
