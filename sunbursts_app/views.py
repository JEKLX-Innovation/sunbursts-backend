from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Sunburst
from .permissions import IsOwnerOrReadOnly
from .serializers import SunburstSerializer


class SunburstList(ListCreateAPIView):
    queryset = Sunburst.objects.all()
    serializer_class = SunburstSerializer


class SunburstDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Sunburst.objects.all()
    serializer_class = SunburstSerializer
