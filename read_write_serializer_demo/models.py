from django.db import models


class ReadWriteFieldDemoModel(models.Model):
    str_field = models.TextField(help_text="列表拼接成字符串字段")
