# Generated by Django 5.1.4 on 2025-01-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]
