from django.shortcuts import render

from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from .permissions import IsEventOwner

def index(request):
    return render(request, 'index.html')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsEventOwner]

