# Generated by Django 4.2.4 on 2023-08-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='First_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
