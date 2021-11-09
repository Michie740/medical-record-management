from django.urls import path
from django.views.generic import RedirectView
from records import views as record_views

urlpatterns = [
    path('add/<pk>/',
         record_views.RecordAddView.as_view(),
         name='add_record'),
    path('list/<pk>/',
         record_views.RecordListView.as_view(),
         name='list_records'),
]
