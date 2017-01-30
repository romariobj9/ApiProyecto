from django.forms import widgets
from rest_framework import serializers
from appInstituciones.models import Universidad,Hospital,Terminal,Aeropuerto,Empresas
    


class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad 
        fields = ('id', 'nombre', 'ciudad', 'latitud', 'longitud')

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital 
        fields = ('id', 'nombre', 'ciudad', 'latitud', 'longitud')

class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal 
        fields = ('id', 'nombre', 'ciudad', 'latitud', 'longitud')   

class AeropuertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeropuerto 
        fields = ('id', 'nombre', 'ciudad', 'latitud', 'longitud')

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas 
        fields = ('id', 'nombre', 'ciudad', 'latitud', 'longitud')                