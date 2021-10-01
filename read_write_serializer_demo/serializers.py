from typing import List, Type

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from read_write_serializer_demo.models import ReadWriteFieldDemoModel
from tools.serializer.fields import ReadWriteSerializerMethodField


class ReadWriteFieldSerializer(serializers.ModelSerializer):
    list_field = ReadWriteSerializerMethodField(help_text="Test ReadWriteFieldSerializer")

    class Meta:
        model = ReadWriteFieldDemoModel
        fields = ["list_field"]

    def get_list_field(self, obj) -> List[str]:
        return [content for content in obj.str_field.split(",")]

    def set_list_field(self, data):
        return {"str_field": ",".join(data)}


class ReadMethodSerializer(serializers.ModelSerializer):
    list_field = SerializerMethodField(help_text="Test SerializerMethodField")

    class Meta:
        model = ReadWriteFieldDemoModel
        fields = ("list_field",)

    def get_list_field(self, obj) -> List[str]:
        return [content for content in obj.str_field.split(",")]


class NaiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadWriteFieldDemoModel
        fields = "__all__"
