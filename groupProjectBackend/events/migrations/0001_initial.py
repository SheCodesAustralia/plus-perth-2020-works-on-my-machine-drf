# Generated by Django 3.0.8 on 2020-11-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('event_city', models.CharField(blank=True, max_length=200, null=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_type', models.CharField(blank=True, max_length=200, null=True)),
                ('event_start', models.DateTimeField(max_length=200)),
                ('event_end', models.DateTimeField(max_length=200)),
                ('event_location', models.CharField(blank=True, max_length=200, null=True)),
                ('all_day', models.BooleanField(default=False)),
            ],
        ),
    ]
