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
def getEntry(request):
    if request.method == 'GET':
        entry = Entry.objects.all()
        serializer = EntrySerializer(entry, many=True)
        return JsonResponse({"entries":serializer.data})

@api_view(['POST'])
def addEntry(request):
    serializer = EntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data)

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
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            entry = Entry.objects.filter(dateTime=request.data)
        
        return JsonResponse({"entries":serializer.data})




