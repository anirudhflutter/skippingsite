# Generated by Django 4.0.5 on 2022-06-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skippings', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='reason',
            field=models.CharField(max_length=100),
        ),
    ]