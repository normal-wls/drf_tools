# Generated by Django 3.2 on 2021-09-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='书名', max_length=255)),
                ('page', models.IntegerField(help_text='页数')),
            ],
        ),
    ]
