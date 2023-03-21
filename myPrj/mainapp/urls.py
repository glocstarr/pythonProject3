from django.urls import path
from .views import translate

urlpatterns = [
    path('', translate, name='home'), # This line defines the root URL pattern
    path('translate/', translate, name='translate'),
    # ... other URL patterns ...
]
