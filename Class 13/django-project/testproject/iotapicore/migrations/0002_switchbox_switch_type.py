# Generated by Django 3.1.3 on 2020-11-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotapicore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='switchbox',
            name='switch_type',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]