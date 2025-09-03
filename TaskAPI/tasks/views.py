from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class TaskViewSet(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  permission_classes = [IsOwner, IsAuthenticated]
  # allows only authenticated and owner (custom permission) user access

  def get_queryset(self):
    return Task.objects.filter(owner=self.request.user)

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  @action(detail=True, methods=["post"])
  def complete(self, request, pk=None):
    task = self.get_object()
    task.status = "Completed"
    task.completed_at = now()
    task.save()
    return Response({"status": "Task marked as completed"})

  @action(detail=True, methods=["post"])
  def incomplete(self, request, pk=None):
    task = self.get_object()
    task.status = "Pending"
    task.completed_at = None
    task.save()
    return Response({"status": "Task marked as incomplete"})