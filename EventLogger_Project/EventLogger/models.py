from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    createDate = models.CharField(max_length=50)

class Entry(models.Model):
    event = models.ForeignKey("Event", verbose_name=("Event"), on_delete=models.CASCADE)
    entry = models.TextField()
    entryDate = models.DateTimeField(auto_now=True)
