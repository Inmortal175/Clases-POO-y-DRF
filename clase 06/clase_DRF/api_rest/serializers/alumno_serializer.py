from rest_framework import serializers
from api_rest.models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['nombre', 'curso', 'id']
        

class AlumnoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['correo', 'curso']

class AlumnoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellidos', 'correo', 'curso']