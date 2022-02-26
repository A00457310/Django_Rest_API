from django.urls import path
from . import views

urlpatterns = [
    path("hotels/", views.HotelList.as_view(), name="hotelGetPost"),
    path("hotels/<int:id>", views.HotelDetail.as_view(), name="hotelDetailsById")


]
