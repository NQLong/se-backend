# Generated by Django 3.1.3 on 2021-10-30 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_file', '0001_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantbanner',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='image_restaurant_banner', to='media_file.media'),
            preserve_default=False,
        ),
    ]