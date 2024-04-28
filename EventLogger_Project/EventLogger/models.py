from django.db import models
import os

class Event(models.Model):
    name = models.CharField(max_length=200, unique=True)
    createDate = models.CharField(max_length=50)
    def __str__(self):
        return f"Event:{self.name}"
    
    def populate(self, path="C:\\Users\\nathe\\Desktop\\Projects\\EventLogger\\Test"):
        results = []
        for f in os.listdir(path):
            if f.endswith('.txt'):
                print(f)
                print(os.path.getctime(path + "/" + f))
                results.append(f)
        return (results)

event = Event()
print(event.populate())
class Entry(models.Model):
    event = models.ForeignKey("Event", verbose_name=("Event"), on_delete=models.CASCADE)
    entry = models.TextField()
    entryDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.entry}"