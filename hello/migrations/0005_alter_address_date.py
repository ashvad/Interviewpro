# Generated by Django 4.0.3 on 2022-04-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_alter_address_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Date',
            field=models.DateField(),
        ),
    ]
