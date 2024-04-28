from django.shortcuts import render, redirect
from django.http import JsonResponse
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

def home(request):
    events = Event.objects.all()
    context = {"Events":events}
    
    return render(request, "index.html", context)


def handleEventClick(request, *args, **kwargs):
    if request.method == "GET":
        print("request is")
        print(request)
        print(str(request)[20:26:])
        print("--------------")
        eventName = str(request)[20:26:]
        entries = Entry.objects.filter(event=eventName)
        context = {"eventEntries":entries}
        return render(request, "index.html", context)

@api_view(['GET'])
def listEntries(request, event_id):
    if request.method == 'GET':
        entry = Entry.objects.filter(event=event_id)   
        serializer = EntrySerializer(entry, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listEvents(request):
    if request.method == 'GET':
        data = Event.objects.all()
        serializer = EventSerializer(data, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
@csrf_exempt
def addEntry(request):
    print(request.data)
    serializer = EntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response("Save Failed")

# Returning the entries for a specific event
@api_view(['GET'])
def getEntries(request, event):
    if request.method == 'GET':
        entry = Entry.objects.filter(event=event)
        serializer = EntrySerializer(entry, many=True)
        return JsonResponse({"entries":serializer.data})

@api_view(['DELETE'])
def deleteEntry(request):
    if request.method == 'DELETE':
        print(request.data)
        event = request.data["event"]
        entryData = request.data["entry"]
        entryDate = request.data["entryDate"]
        entry = Entry.objects.get(event=event, entry=entryData)
        entry.delete() 
        return Response("Item deleted")
    

@api_view(['GET'])
def getEntry(request, event, id):
    if request.method == 'GET':
        entry = Entry.objects.filter(pk=id, event=event)
        serializer = EntrySerializer(entry, many=True)
        return Response(serializer.data)



