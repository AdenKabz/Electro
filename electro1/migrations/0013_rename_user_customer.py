# Generated by Django 5.1.3 on 2024-12-09 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electro1', '0012_alter_userprofile_prof'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]
