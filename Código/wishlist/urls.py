from django.contrib import admin
from django.urls import path, include  # ← Add include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # ← Include app URLs
]