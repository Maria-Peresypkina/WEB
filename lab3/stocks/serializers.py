from stocks.models import Accommodation, Guest, Booking
from rest_framework import serializers


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Accommodation
        # Поля, которые мы сериализуем
        fields = ["pk", "acc_name", "location", "description", "price", "contacts"]

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Guest
        # Поля, которые мы сериализуем
        fields = ["pk", "guest_name", "city", "country", "email", "phone"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        # Поля, которые мы сериализуем
        fields = ["pk", "guest_id", "accommodation_id", "dates"]