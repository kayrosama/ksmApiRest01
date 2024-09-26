from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from apps.models import Humanos
from apps.apis.serializer import HumanosSerializer
from apps.apis.permissions import IsAdminOrReadOnly 

# Tercera forma usando ModelViewSet
class HumanosModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = HumanosSerializer
    queryset = Humanos.objects.all()

#
# Segunda Forma usando ViewSet 
#class HumanoViewSet(ViewSet):
#    def list(self, request):
#        serializer = HumanosSerializer(Humanos.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#    
#    def retrieve(self, request, pk: int):
#        vapp = HumanosSerializer(Humanos.objects.get(pk=pk))
#        return Response(status=status.HTTP_200_OK, data=vapp.data)
#    
#    def create(self, request):
#        serializer = HumanosSerializer(data=request.POST)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#    
# Primera forma usando APIView
#class HumanoApiView(APIView):
#    def get(self, request):
#        serializer = HumanosSerializer(Humanos.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#    
#    def post(self, request):
#        serializer = HumanosSerializer(data=request.POST)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#
