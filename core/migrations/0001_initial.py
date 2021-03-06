# Generated by Django 4.0.1 on 2022-01-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(blank=True, max_length=100, null=True)),
                ('acc', models.IntegerField(blank=True, null=True)),
                ('alt', models.IntegerField(blank=True, null=True)),
                ('batt', models.IntegerField(blank=True, null=True)),
                ('bs', models.IntegerField(blank=True, null=True)),
                ('conn', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('t', models.IntegerField(blank=True, null=True)),
                ('tid', models.CharField(blank=True, max_length=100, null=True)),
                ('topic', models.CharField(blank=True, max_length=100, null=True)),
                ('tst', models.IntegerField(blank=True, null=True)),
                ('vac', models.IntegerField(blank=True, null=True)),
                ('vel', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocationEntryJson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
