# Generated by Django 5.1.3 on 2024-12-09 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro1', '0013_rename_user_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='prof',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electro1.customer'),
        ),
    ]
