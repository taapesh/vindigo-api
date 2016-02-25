from rest_framework import serializers

from models import VindigoUser, Device, Trip, Vehicle

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = VindigoUser
        fields = (
            "email",
        )

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = (
            "device_id",
            "device_name",
            "time_created",
            "vehicle_id",
            "time_driven",
            "distance_driven",
            "location_address",
            "location_lat",
            "location_lng",
        )

class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = (
            "trip_id",
            "status",
            "time_start",
            "time_end",
            "device_id",
            "vehicle_id",
            "distance",
            "duration",
            "current_speed",
            "average_moving_speed",
            "max_speed",
            "average_speed",
            "hard_accel_count",
            "hard_brake_count",
            "stop_count",
            "start_address",
            "end_address",
            "start_lat",
            "start_lng",
            "stop_lat",
            "stop_lng",
        )

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            "vehicle_id",
            "device_id",
            "year",
            "make",
            "model",
            "trim",
        )
