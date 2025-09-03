from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source="owner.username")
  # source ="owner.username" ensures that the name of the logged in user
  # shows instead of the ID of the user. declares owner which is a field in
  # in Task model to be readonly and the value is set automatically to the current logged uer
  #  we can use owner = serializers.PrimaryKeyRelatedField(read_only = True) to just show the ID

  class Meta:
    model = Task
    fields = "__all__"
