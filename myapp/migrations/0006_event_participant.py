# Generated by Django 4.2.4 on 2023-08-13 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_jobposition_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email_id', models.EmailField(max_length=254, unique=True)),
                ('Registration_date', models.DateTimeField(auto_now_add=True)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.event')),
            ],
        ),
    ]