from django.contrib import admin
from django.urls import path, include  # Add include import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth0_auth.urls')),  # Include your app's URLs
]
