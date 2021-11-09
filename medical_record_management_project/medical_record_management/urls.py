from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('patients/', include('patients.urls')),
    path('records/', include('records.urls'))
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
