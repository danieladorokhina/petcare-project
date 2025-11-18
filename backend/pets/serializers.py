from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("id", "name", "species", "age", "notes", "created_at")

    def validate_age(self, value):
        if value > 50:
            raise serializers.ValidationError("Вік тварини виглядає підозрілим 🙂")
        return value