from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.vindigo_api),

    # Device API
    url(r"^devices/create_dummy_device", views.create_dummy_device),
    url(r'^devices/(?P<device_id>\w+)/trips', views.get_device_trips),
    url(r'^devices/(?P<device_id>\w+)/latest_vehicle', views.latest_vehicle),
    url(r'^devices/(?P<device_id>\w+)', views.get_device),
    url(r'^devices/(?P<device_id>\w+)', views.get_device_vehicles),

    # Trip API
    url(r'^trips/(?P<trip_id>\w+)', views.get_trip),

    # Vehicle API
    url(r'^vehicles/(?P<vehicle_id>\w+)', views.get_vehicle),
]
