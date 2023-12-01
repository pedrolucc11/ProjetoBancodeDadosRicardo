from rest_framework import serializers
from .models import Jog


class JogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jog
        fields = '__all__'