from rest_framework import status
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import render

from app.models import VindigoUser
from app.serializers import UserSerializer, DeviceSerializer, TripSerializer, VehicleSerializer
