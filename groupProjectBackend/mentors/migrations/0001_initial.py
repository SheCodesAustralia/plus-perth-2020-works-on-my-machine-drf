# Generated by Django 3.0.8 on 2020-11-02 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MentorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_name', models.CharField(max_length=200)),
                ('mentor_email', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('mentor_type', models.CharField(max_length=200)),
                ('one_day_workshop', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MentorProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview', models.BooleanField(default=False)),
                ('interview_completed', models.DateTimeField(blank=True, null=True)),
                ('offer_position', models.BooleanField(default=False)),
                ('offer_position_completed', models.DateTimeField(blank=True, null=True)),
                ('send_contract', models.BooleanField(default=False)),
                ('send_contract_completed', models.DateTimeField(blank=True, null=True)),
                ('signed_contract', models.BooleanField(default=False)),
                ('signed_contract_completed', models.DateTimeField(blank=True, null=True)),
                ('calendar_invites', models.BooleanField(default=False)),
                ('calendar_invites_completed', models.DateTimeField(blank=True, null=True)),
                ('onboarding', models.BooleanField(default=False)),
                ('onboarding_completed', models.DateTimeField(blank=True, null=True)),
                ('feedback', models.BooleanField(default=False)),
                ('feedback_completed', models.DateTimeField(blank=True, null=True)),
                ('offboarding', models.BooleanField(default=False)),
                ('offboarding_completed', models.DateTimeField(blank=True, null=True)),
                ('mentor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='process', to='mentors.MentorProfile')),
            ],
        ),
    ]
