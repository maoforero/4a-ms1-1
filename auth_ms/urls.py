from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')), #endpoint login
    path('rest-auth/registration/', include('rest_auth.registration.urls')) #endpoint registro
]
