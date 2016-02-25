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

@api_view(["GET"])
def get_device(request, device_id):
    try:
        device = Device.objects.get(device_id=device_id)
        serializer = DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Device.DoesNotExist:
        return Response({"error": "Invalid device id"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def latest_vehicle(request, device_id):
    try:
        device = Device.objects.get(device_id=device_id)
        
        if device.vehicle_id is not None:
            vehicle = Vehicle.objects.get(vehicle_id=device.vehicle_id)
            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response({"message": "No vehicle associated with this device"}, status=status.HTTP_200_OK)

    except Device.DoesNotExist:
        return Response({"error": "Invalid device id"})

@api_view(["GET"])
def get_device_trips(request, device_id):
    try:
        device = Device.objects.get(device_id=device_id)

        trips = Trip.objects.filter(device_id=device_id)
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Device.DoesNotExist:
        return Response({"error": "Invalid device id"})
