# Generated by Django 4.2.4 on 2023-08-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_teachers_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]