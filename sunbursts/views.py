from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Sunburst
from .permissions import IsOwnerOrReadOnly
from .serializers import SunburstSerializer


class SunburstListView(ListCreateAPIView):
    queryset = Sunburst.objects.all()
    serializer_class = SunburstSerializer


class SunburstDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Sunburst.objects.all()
    serializer_class = SunburstSerializer
