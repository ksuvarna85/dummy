# Generated by Django 3.0.7 on 2020-09-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoprofile',
            name='verfied',
            field=models.BooleanField(default=False),
        ),
    ]