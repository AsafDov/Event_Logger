from django.db import models
from django.db.utils import IntegrityError
import os
import time
import json
import manage

class Event(models.Model):
    name = models.CharField(max_length=200, unique=True)
    createDate = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Event: {self.name}"
    
    def populate(self, path="C:\\Users\\nathe\\Desktop\\Projects\\EventLogger\\Test"):
        results = []
        allEvents = Event.objects.all()
        for f in os.listdir(path):
            if f.endswith('.txt'):
                created = time.ctime(os.path.getctime(path + "/" + f))
                event = {
                    "name": f,
                    "createDate":created
                }
                try:
                    Event.objects.get(name=event["name"])
                    continue
                except Event.DoesNotExist:
                    e = Event(name=event["name"], createDate=event["createDate"] )
                    e.save()
                    continue

        results.append(event)
        return (results)

eventDB = Event()
eventDB.populate()


class Entry(models.Model):
    event = models.ForeignKey("Event", verbose_name=("Event"), on_delete=models.CASCADE)
    entry = models.TextField()
    entryDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.entry}"