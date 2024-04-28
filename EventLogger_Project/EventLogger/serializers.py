from rest_framework import serializers
from .models import *

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['event', 'entry', 'entryDate']
    
    entryDate = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    entryDate = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)