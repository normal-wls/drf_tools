from rest_framework.viewsets import ModelViewSet

from demos.models import ReadWriteFieldDemoModel
from demos.serializers import ReadWriteFieldSerializer


class ReadWriteFieldViewSet(ModelViewSet):
    serializer_class = ReadWriteFieldSerializer
    queryset = ReadWriteFieldDemoModel.objects.all()
