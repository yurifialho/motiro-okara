# Generated by Django 3.2.8 on 2021-10-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kipco', '0002_intensiveprocess'),
    ]

    operations = [
        migrations.AddField(
            model_name='intensiveprocess',
            name='storeid',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
