# Generated by Django 4.0.3 on 2022-04-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_alter_address_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Ip_address',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]