# Generated by Django 4.2.4 on 2023-08-11 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('L_name', models.CharField(max_length=100)),
                ('Phnno', models.IntegerField(null=True)),
                ('Departments', models.CharField(max_length=100)),
                ('Mail_id', models.CharField(max_length=100)),
            ],
        ),
    ]
