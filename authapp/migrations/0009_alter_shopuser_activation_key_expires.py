# Generated by Django 3.2.11 on 2022-01-28 16:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 30, 16, 7, 20, 916683, tzinfo=utc), verbose_name='Срок активации'),
        ),
    ]
