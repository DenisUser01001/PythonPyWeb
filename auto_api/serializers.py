from rest_framework import serializers

from automobile.models import Auto


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = "__all__"
