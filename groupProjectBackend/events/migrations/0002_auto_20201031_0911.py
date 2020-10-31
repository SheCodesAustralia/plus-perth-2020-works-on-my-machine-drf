# Generated by Django 3.0.8 on 2020-10-31 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='mentor_list',
            field=models.ManyToManyField(related_name='event_attending', related_query_name='mentor_attending', to='mentors.MentorProfile'),
        ),
    ]