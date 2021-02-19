from rest_framework.serializers import ModelSerializer
from .models import Propiedad

class PropiedadSerializer(ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'