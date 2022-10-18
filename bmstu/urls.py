from bmstu_lab import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.AllGuests),
    #path('guest/<int:id>/', views.GetGuest, name='guest_url'),
    path('', views.accommodationList),
    path('accommodation/<int:id>/', views.GetAccommodation, name='accommodation_url'),
    #path('showall/', views.accommodationList),
    #path('admin/', admin.site.urls),
    #path('', views.GetOrders),
    #path('order/<int:id>/', views.GetOrder, name='order_url'),
]
