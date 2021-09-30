from typing import List, Type

from rest_framework import serializers

from demos.models import ReadWriteFieldDemoModel
from tools.serializer.fields import ReadWriteSerializerMethodField


class ReadWriteFieldSerializer(serializers.ModelSerializer):
    list_field = ReadWriteSerializerMethodField(help_text="Test")

    class Meta:
        model = ReadWriteFieldDemoModel
        fields = ["list_field"]

    def get_list_field(self, obj) -> List[str]:
        return [content for content in obj.str_field.split(",")]

    def set_list_field(self, data):
        return {"str_field": ",".join(data)}
