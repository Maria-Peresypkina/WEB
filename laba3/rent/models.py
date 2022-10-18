from django.db import models


class Stock(models.Model):
    company_name = models.CharField(max_length=50, verbose_name="Название компании")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена акции")
    is_growing = models.BooleanField(verbose_name="Растет ли акция в цене?")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз обновлялось значение акции?")


class Accommodation(models.Model):
    acc_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=30)
    contacts = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'accommodation'


class Guest(models.Model):
    guest_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'guests'


class Booking(models.Model):
    guest_id = models.IntegerField()
    accommodation_id = models.IntegerField()
    dates = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'bookings'