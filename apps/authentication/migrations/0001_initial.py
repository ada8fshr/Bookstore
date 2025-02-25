# Generated by Django 4.2.1 on 2023-05-27 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.TextField(default='Not set')),
                ('bio', models.TextField(default='Not set')),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='profilePics/')),
                ('subscribed_to', models.ManyToManyField(blank=True, related_name='subscribed_to', to=settings.AUTH_USER_MODEL)),
                ('subscribers', models.ManyToManyField(blank=True, related_name='subscribers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
