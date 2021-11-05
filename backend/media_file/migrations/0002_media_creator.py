# Generated by Django 3.1.3 on 2021-11-04 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media_file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
