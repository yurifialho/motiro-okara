# Generated by Django 3.2.8 on 2022-04-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kipco', '0007_auto_20220412_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentspecialty',
            name='storid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agenttype',
            name='storid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
