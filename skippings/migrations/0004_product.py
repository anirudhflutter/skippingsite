# Generated by Django 4.0.5 on 2022-06-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skippings', '0003_person_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('productimage', models.CharField(max_length=100)),
                ('productprice', models.IntegerField()),
            ],
        ),
    ]