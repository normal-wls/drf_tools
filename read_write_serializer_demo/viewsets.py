from rest_framework.viewsets import ModelViewSet

from read_write_serializer_demo.models import ReadWriteFieldDemoModel
from read_write_serializer_demo.serializers import ReadWriteFieldSerializer, ReadMethodSerializer

from read_write_serializer_demo.serializers import NaiveSerializer


class ReadWriteFieldViewSet(ModelViewSet):
    serializer_class = ReadWriteFieldSerializer
    queryset = ReadWriteFieldDemoModel.objects.all()
