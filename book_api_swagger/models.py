from django.db import models


class Book(models.Model):
    name = models.CharField(help_text="书名", max_length=255)
    page = models.IntegerField(help_text="页数")
