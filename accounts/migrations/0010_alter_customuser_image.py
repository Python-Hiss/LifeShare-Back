# Generated by Django 4.0 on 2022-01-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customuser_email_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='../files/image/profileiamge.jpg', null=True, upload_to='image'),
        ),
    ]
