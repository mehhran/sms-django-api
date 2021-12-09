from smsApp.views import SMSAPIView, SmsViewSet, BatteryAPIView, BatteryViewSet
from django.urls import path



urlpatterns = [
    path("", SMSAPIView.as_view() , name="sms"),
    path("list/", SmsViewSet.as_view({'get':'list'}), name="SMSList"),
    path("battery/", BatteryAPIView.as_view(), name="BatteryPct"),
    path("battery/list/", BatteryViewSet.as_view({'get':'list'}), name="BatteryPctList"),
]