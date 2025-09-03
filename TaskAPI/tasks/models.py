from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class Task(models.Model):
  PRIORITY_CHOICES = [
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
  ]
  #  an enum to determine priority level

  STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Completed", "Completed"),
  ]
  # an emum to determine the status of tasks

  title = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  deadline = models.DateField()
  priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="Medium")
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")
  completed_at = models.DateTimeField(null=True, blank=True)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")

  def __str__(self):
    return self.title