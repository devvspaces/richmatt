# Generated by Django 3.2.2 on 2021-05-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Ladies'), ('boys', 'Boys'), ('girls', 'Girls')], max_length=10),
        ),
    ]