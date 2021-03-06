# Generated by Django 3.1.3 on 2021-11-04 23:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDeviceToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('key', models.TextField(null=True)),
                ('device_type', models.CharField(choices=[('IOS', 'Ios'), ('ANDROID', 'Android'), ('WEBAPP', 'Webapp')], default='WEBAPP', max_length=16)),
                ('client_ip', models.CharField(max_length=56)),
                ('device_id', models.CharField(blank=True, max_length=36, null=True)),
                ('device_token', models.CharField(blank=True, max_length=163, null=True)),
                ('device_model', models.CharField(blank=True, max_length=64, null=True)),
                ('user_agent', models.TextField(blank=True, default='', null=True)),
                ('active', models.BooleanField(default=False)),
                ('deactivated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
