from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rent.serializers import AccommodationSerializer
from rent.serializers import GuestSerializer
from rent.serializers import BookingSerializer
from rent.models import Accommodation, Guest, Booking


class AccommodationViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Accommodation.objects.all().order_by('pk')
    serializer_class = AccommodationSerializer  # Сериализатор для модели


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all().order_by('pk')
    serializer_class = GuestSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('pk')
    serializer_class = BookingSerializer

