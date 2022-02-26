from rest_framework import serializers
from hotelAppp.models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hotel
        fields=['id','hotel_name','address','capacity']