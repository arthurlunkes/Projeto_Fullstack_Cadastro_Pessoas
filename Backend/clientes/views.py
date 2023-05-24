from rest_framework import viewsets
from serializer import ClienteSerializer
from models import Cliente
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
