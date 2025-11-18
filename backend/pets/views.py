from rest_framework import viewsets, permissions
from .models import Pet
from .serializers import PetSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class PetViewSet(viewsets.ModelViewSet):
    """
    CRUD для тварин поточного користувача:
    GET /api/pets/
    POST /api/pets/
    GET /api/pets/<id>/
    PUT/PATCH/DELETE /api/pets/<id>/
    """
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Pet.objects.filter(owner=request.user)

    def perform_create(self, serializer):
        serializer.save(owner=request.user)