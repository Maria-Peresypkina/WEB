from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from stocks.serializers import AccommodationSerializer
from stocks.serializers import GuestSerializer
from stocks.serializers import BookingSerializer
from stocks.models import Accommodation, Guest, Booking


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

