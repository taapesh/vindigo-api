from rest_framework import status
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from datetime import datetime, timedelta

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
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(DeviceSerializer(device), status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_device(request, device_id):
    try:
        device = Device.objects.get(device_id=device_id)
        serializer = DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Device.DoesNotExist:
        return Response({"error": "Device does not exist"}, status=status.HTTP_404_NOT_FOUND)

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
        return Response({"error": "Device does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def get_device_trips(request, device_id):
    try:
        device = Device.objects.get(device_id=device_id)
        trips = Trip.objects.filter(device_id=device_id)
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Device.DoesNotExist:
        return Response({"error": "Device does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def get_trip(request, trip_id):
    try:
        trip = Trip.objects.get(trip_id=trip_id)
        serializer = TripSerializer(trip)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Trip.DoesNotExist:
        return Response({"error": "Trip does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_trip(request):
    serializer = TripSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_device_vehicles(request, device_id):
    try:
        device = Device.objects.get(device_id=device_id)
        vehicles = Vehicle.objects.filter(device_id=device_id)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Device.DoesNotExist:
        return Response({"error": "Device does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def get_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def register_vehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(VehicleSerializer(vehicle).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
        vehicle.delete()
        return Response({"message": "Vehicle deleted"}, status=status.HTTP_200_OK)
    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle does not exist"}, status=status.HTTP_404_NOT_FOUND)

