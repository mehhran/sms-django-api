# Generated by Django 4.0 on 2021-12-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batteryPct', models.FloatField()),
                ('action', models.CharField(max_length=100)),
                ('action_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('receiver', models.CharField(max_length=100)),
            ],
        ),
    ]