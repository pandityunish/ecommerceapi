from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class LocationAPIView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Location.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)
