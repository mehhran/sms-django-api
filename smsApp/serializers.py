from smsApp.models import Sms, BatteryLevel
from rest_framework import serializers

class SmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sms
        fields = ['sender', 'body', 'datetime', 'receiver']

class BatteryLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BatteryLevel
        fields = ['batteryPct', 'action', 'action_time']