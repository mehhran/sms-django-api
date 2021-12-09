import requests

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from smsApp.models import Sms, BatteryLevel
from smsApp.serializers import SmsSerializer, BatteryLevelSerializer

import dateutil.parser

from smsProject.secrets import sms_chat_id, battery_chat_id, telegram_bot_token

class SMSAPIView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        
        return Response({"message": "Hello, world!"})

    def post(self, request):

        mdu = str("From: "+request.data["sender"]+"\nTo: "+request.data["receiver"]+"\nMessage: "+request.data["body"])

        pload = {"chat_id": sms_chat_id, "text":"<pre>"+mdu+"</pre>", 
                  "parse_mode":"HTML"}
        
        try:
            r = requests.post(str('https://api.telegram.org/'+telegram_bot_token+'/sendMessage'), data=pload)
            bot_sent = True
        except:
            bot_sent = False

        try:
            sms = Sms(sender=request.data["sender"], body=request.data["body"], receiver=request.data["receiver"])
            sms.save()
            saved = True
        except:
            saved = False

        return Response({"message": "Got some data!", "data": r, "sms_saved": saved, "bot_sent": bot_sent})


class SmsViewSet(viewsets.ModelViewSet):
    
    queryset = Sms.objects.all().order_by('-datetime')
    serializer_class = SmsSerializer
    permission_classes = [IsAdminUser]

class BatteryAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        
        return Response({"message": "Hello, world!"})

    def post(self, request):

        formatted_action_time = dateutil.parser.parse(request.data['action_time'])
        batteryPct = float(request.data["batteryPct"])
        action = request.data["action"]

        batteryLevel = BatteryLevel(batteryPct=batteryPct, action=action, action_time=formatted_action_time)
        
        try:
            batteryLevel.save()
            saved = True
        except:
            saved = False

        mdu = str("batteryPct: "+ str(batteryPct) +"\nAction: "+ action)

        pload = {"chat_id": battery_chat_id, "text":"<pre>"+mdu+"</pre>", 
                  "parse_mode":"HTML"}
        
        try:
            r = requests.post(str('https://api.telegram.org/'+telegram_bot_token+'/sendMessage'), data=pload)
            bot_sent = True
        except:
            bot_sent = False

        return Response({"message": "Got some data!", "pct_saved": saved, "bot_sent": bot_sent})


class BatteryViewSet(viewsets.ModelViewSet):

    queryset = BatteryLevel.objects.all().order_by('-action_time')
    serializer_class = BatteryLevelSerializer
    permission_classes = [IsAdminUser]