# Generated by Django 4.0 on 2022-01-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donating', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
