from io import StringIO
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import csv
from django.core.files.storage import default_storage

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

@api_view(['GET'])
def loadEvents(request):
    if request.method == 'GET':
        loader = Event()
        loader.populate() #Enter Path veriable
        return Response("Success")
        
    
@api_view(['POST', 'GET'])
@csrf_exempt
def addEntry(request):
    print(f"Entry added {request.data} ")
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
        print(f"DELETE: {request.data}")
        event = request.data["event"]
        entryData = request.data["entry"]
        entryDate = request.data["entryDate"]
        entry = Entry.objects.filter(event=event, entry=entryData)
        entry.delete() 
        return Response("Item deleted")
    

@api_view(['GET'])
def getEntry(request, event, id):
    if request.method == 'GET':
        entry = Entry.objects.filter(pk=id, event=event)
        serializer = EntrySerializer(entry, many=True)
        return Response(serializer.data)



def export_data_to_csv(request, model_name):
    
    path = "C:/Users/nathe/Desktop/Projects/EventLogger/Test"
    filename = "Event_Log.csv"

    with open(f"{path}/{filename}", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = [field.name for field in Event._meta.fields if field.name != 'id'] + [field.name for field in Entry._meta.fields if (field.name != 'id' and field.name != 'event')]
        writer.writerow(header) #Write header row
    
        model_data = Event.objects.all()
        for event in model_data:
            event_row = [getattr(event, field.name) for field in Event._meta.fields if field.name != 'id']
            entries = Entry.objects.filter(event=event)
            for entry in entries:
                entry_row = [getattr(entry, field.name) for field in Entry._meta.fields if (field.name != 'id' and field.name != 'event') ]
                entry_row[1]=str(entry_row[1])[:19]
                data_row=event_row + entry_row
                # Extract data from each model object and format as a list
                writer.writerow(data_row)

    return Response("CSV saved successfuly")
