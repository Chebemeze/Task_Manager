from rest_framework.permissions import BasePermission

# adding a custom permission that ensures users can only access their tasks
# which will later be imported into permission_classes in viewset
class IsOwner(BasePermission):
  def has_object_permission(self, request, view, obj):
    return getattr(obj, "owner_id", None) == request.user.id
