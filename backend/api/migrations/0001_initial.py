# Generated by Django 5.1.3 on 2024-11-17 00:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('host_endpoint', models.CharField(max_length=50)),
                ('host_username', models.CharField(max_length=50)),
                ('host_password', models.CharField(max_length=150)),
                ('host_port', models.PositiveIntegerField()),
                ('data_create', models.DateTimeField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SQL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('sql', models.TextField()),
                ('data_create', models.DateTimeField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('data_cron', models.CharField(max_length=100)),
                ('data_json', models.JSONField()),
                ('type_chart', models.IntegerField(default=1)),
                ('emphasis', models.BooleanField(default=False)),
                ('data_create', models.DateTimeField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.host')),
                ('sql', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sql')),
            ],
        ),
    ]
