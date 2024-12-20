# Generated by Django 5.1.3 on 2024-12-07 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro1', '0006_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='electro1.user')),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('meter_number', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
