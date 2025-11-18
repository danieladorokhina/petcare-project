from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("id", "pet", "vet", "date", "status", "notes", "created_at")
        read_only_fields = ("status", "created_at")

    def validate(self, attrs):
        # приклад простої валідації: дата з майбутнього
        from django.utils import timezone

        if attrs["date"] <= timezone.now():
            raise serializers.ValidationError("Дата візиту має бути у майбутньому.")
        return attrs