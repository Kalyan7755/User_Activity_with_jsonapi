from django.db import models
import datetime

class User_Act(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=100)
    start_time = models.DateTimeField(("Date"), default=datetime.date.today)
    end_time = models.DateTimeField(("Date"), default=datetime.date.today)

