# Generated by Django 5.1.2 on 2024-10-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_remove_qr_qr_image_qrimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrimage',
            name='qr_image',
            field=models.ImageField(upload_to='qr.png'),
        ),
    ]
