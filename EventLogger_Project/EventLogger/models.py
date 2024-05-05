from django.db import models
from django.db.utils import IntegrityError
import os
import time

class Event(models.Model):
    name = models.CharField(max_length=200, unique=True)
    createDate = models.CharField(max_length=50)

    class Meta:
        ordering = ['-createDate']
    
    def __str__(self):
        return f"Event: {self.name}"
    
    def populate(self, path="C:\\Users\\nathe\\Desktop\\Projects\\EventLogger\\Test"):
        results = []
        allEvents = Event.objects.all()
        for (root, dirs, file) in os.walk(path):
            for f in file:
                if '.gcd' in f or '.gcm' in f or '.txt' in f: #Change to txt for testing
                    filepath = os.path.join(root, f)
                    print(filepath)
                    created = time.ctime(os.path.getctime(root + "\\" + f))
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
                        results.append(event)
                        continue
        return (results)



class Entry(models.Model):
    event = models.ForeignKey("Event", verbose_name=("Event"), on_delete=models.CASCADE)
    entry = models.TextField()
    entryDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.entry}"