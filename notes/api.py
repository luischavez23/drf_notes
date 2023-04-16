from rest_framework import viewsets, permissions

from .models import Notes
from .serializer import NotesSerializer

class NotesViewSets(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NotesSerializer