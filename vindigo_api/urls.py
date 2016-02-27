from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.vindigo_api),

    # Device API
    url(r'devices/reset_device', views.reset_device),
    url(r'^devices/create_dummy_device', views.create_dummy_device),
    url(r'^devices/(?P<device_id>\w+)/trips', views.get_device_trips),
    url(r'^devices/(?P<device_id>\w+)/latest_vehicle', views.latest_vehicle),
    url(r'^devices/(?P<device_id>\w+)/vehicles', views.get_device_vehicles),
    url(r'^devices/all', views.get_all_devices),
    url(r'^devices/(?P<device_id>\w+)', views.get_device),

    # Trip API
    url(r'^trips/log_trip', views.log_trip),
    url(r'^trips/(?P<trip_id>\w+)', views.get_trip),

    # Vehicle API
    url(r'^vehicles/register_vehicle', views.register_vehicle),
    url(r'^vehicles/(?P<vehicle_id>\w+)', views.get_vehicle),
]
