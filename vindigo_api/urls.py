from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.vindigo_api),

    # Device API
    url(r"^devices/create_dummy_device/", views.create_dummy_device),

    # API Roots
    url(r"devices/", views.devices_api),
    url(r"^trips/", views.trips_api),
    url(r"^vehicles/", views.vehicles_api),    
]
