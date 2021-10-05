from django.urls import path
from django.views.generic import RedirectView
from patients import views as patient_views

urlpatterns = [
    path('list/',
         patient_views.PatientListView.as_view(),
         name='patient_list'),
    path('', RedirectView.as_view(url='login/handle/', permanent=False)),
]
