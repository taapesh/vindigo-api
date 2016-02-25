from rest_framework import status
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import render

from app.models import VindigoUser, Device, Trip, Vehicle
from app.serializers import UserSerializer, DeviceSerializer, TripSerializer, VehicleSerializer

@api_view()
def vindigo_api(request):
    """ Vindigo API """
    return Response({
        "Devices API": "http://127.0.0.1:8000/devices/",
        "Trips API": "http://127.0.0.1:8000/trips/",
        "Vehicles API": "http://127.0.0.1:8000/vehicles/"
    })

@api_view()
def devices_api(request):
    """ Vindigo Device API """
    return Response({
        "Create a dummy device": "http://127.0.0.1:8000/devices/create_dummy_device/",
        "List all devices": "http://127.0.0.1:8000/",
        "Get a device": "http://127.0.0.1:8000/",
        "List device trips": "http://127.0.0.1:8000/",
        "Latest vehicle": "http://127.0.0.1:8000/"
    })

@api_view()
def trips_api(request):
    """ Vindigo Trip API """
    return Response({
        "Get a trip": "http://127.0.0.1:8000/"    
    })
 
@api_view()
def vehicles_api(request):
    """ Vindigo Vehicle API """
    return Response({
        "Get a vehicle": "http://127.0.0.1:8000/"    
    })

@api_view(["POST"])
def create_dummy_device(request):
    """ Create a device for testing purposes """

    device_name = request.data.get("device_name")

    device = Device()
    device.save()

    # For now, use the simple unique id of the device
    # In production, we would generate a strong unique id for each device
    device.device_id = str(device.id)
    
    if device_name is not None:
        device.device_name = device_name
    
    device.save()

    serializer = DeviceSerializer(device)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


