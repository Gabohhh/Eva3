from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializers

# Create your views here.

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all().order_by('-create_at')
    serializer_class = TareaSerializers