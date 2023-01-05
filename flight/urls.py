from django.urls import path
from .views import FlightView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("flights", FlightView)

urlpatterns = [
    
]
urlpatterns += router.urls