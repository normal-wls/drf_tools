# Generated by Django 2.2.24 on 2021-12-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('book_api_swagger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
