
from rest_framework import viewsets 
from .models import Jog
from .serializers import JogSerializer


class JogViewset(viewsets.ModelViewSet):
    queryset = Jog.objects.all()
    serializer_class = JogSerializer
