# Generated by Django 5.1.3 on 2024-12-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro1', '0025_alter_customer_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_number', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
