from django.urls import path
from django.views.generic import RedirectView
from patients import views as patient_views

urlpatterns = [
    path('list/',
         patient_views.PatientListView.as_view(),
         name='patient_list'),
    path('', RedirectView.as_view(url='login/handle/', permanent=False)),
    path('add_patient/', 
         patient_views.PatientAddView.as_view(),
         name='add_patient'),
    path('edit_patient/<pk>/',
         patient_views.PatientEditView.as_view(),
         name='edit_patient'),
    path('add_address/', 
         patient_views.AddressAddView.as_view(),
         name='add_address'),
]
