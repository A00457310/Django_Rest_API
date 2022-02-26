from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from hotelAppp.models import Hotel
from hotelAppp.hotelSerializer import HotelSerializer
from rest_framework import status
from django.http import Http404


# Create your views here.
class HotelList(APIView):

    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelDetail(APIView):
    def get_object(self, id):
        try:
            return Hotel.objects.get(id=id)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, id):
        hotel = self.get_object(id)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    def put(self, request, id):
        hotel = self.get_object(id)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        hotel = self.get_object(id)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
