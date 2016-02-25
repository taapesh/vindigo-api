from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.vindigo_api),

    # Device API
    url(r"^devices/create_dummy_device", views.create_dummy_device),
    url(r'^devices/(?P<device_id>\w+)/latest_vehicle', views.latest_vehicle),
    url(r'^devices/(?P<device_id>\w+)', views.get_device), 
]
