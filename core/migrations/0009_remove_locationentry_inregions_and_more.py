# Generated by Django 4.0.1 on 2022-01-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_waypointsentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationentry',
            name='inregions',
        ),
        migrations.AddField(
            model_name='locationentry',
            name='inregions',
            field=models.ManyToManyField(to='core.WaypointEntry'),
        ),
        migrations.AlterField(
            model_name='waypointentry',
            name='desc',
            field=models.CharField(default='temp', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
