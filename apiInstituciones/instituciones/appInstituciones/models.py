from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
    
    
class Universidad(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=150, blank=True, default='')
    ciudad = models.CharField(max_length=100, blank=True, default='')
    latitud = models.FloatField(max_length=15, blank=True, default=None)
    longitud = models.FloatField(max_length=15, blank=True, default=None)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
     	return "%s" % (self.nombre)

class Hospital(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=150, blank=True, default='')
    ciudad = models.CharField(max_length=100, blank=True, default='')
    latitud = models.FloatField(max_length=15, blank=True, default=None)
    longitud = models.FloatField(max_length=15, blank=True, default=None)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
		return "%s" % (self.nombre)        	

class Terminal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=150, blank=True, default='')
    ciudad = models.CharField(max_length=100, blank=True, default='')
    latitud = models.FloatField(max_length=15, blank=True, default=None)
    longitud = models.FloatField(max_length=15, blank=True, default=None)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
		return "%s" % (self.nombre)	

class Aeropuerto(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=150, blank=True, default='')
    ciudad = models.CharField(max_length=100, blank=True, default='')
    latitud = models.FloatField(max_length=15, blank=True, default=None)
    longitud = models.FloatField(max_length=15, blank=True, default=None)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
		return "%s" % (self.nombre)	

class Empresas(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=150, blank=True, default='')
    ciudad = models.CharField(max_length=100, blank=True, default='')
    latitud = models.FloatField(max_length=15, blank=True, default=None)
    longitud = models.FloatField(max_length=15, blank=True, default=None)
    
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
		return "%s" % (self.nombre)	