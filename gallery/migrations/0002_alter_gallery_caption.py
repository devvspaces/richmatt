# Generated by Django 3.2.2 on 2021-05-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='caption',
            field=models.TextField(blank=True),
        ),
    ]
