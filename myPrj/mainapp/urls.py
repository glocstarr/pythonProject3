from django.urls import path
from .views import translate

urlpatterns = [
    path('', translate, name='home'), 
    path('translate/', translate, name='translate'),
]
