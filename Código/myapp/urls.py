from django.urls import path
from . import views  # Import from current app

urlpatterns = [
    path('', views.home_view, name='home'),
]