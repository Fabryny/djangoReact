# Generated by Django 3.0 on 2022-07-06 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220705_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
    ]
