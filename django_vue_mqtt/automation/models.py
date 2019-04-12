from django.db import models

# Create your models here.


class Automation(models.Model):
    automation_id = models.AutoField(primary_key=True)
    automation_heading = models.CharField(max_length=250)
    automation_body = models.TextField()
