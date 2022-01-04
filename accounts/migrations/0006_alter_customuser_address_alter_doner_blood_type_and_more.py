# Generated by Django 4.0 on 2022-01-03 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0001_initial'),
        ('blood_donating', '0001_initial'),
        ('accounts', '0005_customuser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.address'),
        ),
        migrations.AlterField(
            model_name='doner',
            name='blood_type',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_donating.bloodtype'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_donating.bloodtype'),
        ),
    ]