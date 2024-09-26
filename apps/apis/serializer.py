from rest_framework.serializers import ModelSerializer
from apps.models import Humanos

class HumanosSerializer(ModelSerializer):
    class Meta:
        model = Humanos
        fields = ['Nombres','ApeUno','ApeDos','ApeTres']

