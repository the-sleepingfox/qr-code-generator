# Generated by Django 5.1.2 on 2024-10-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_alter_qrimage_qr_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrimage',
            name='qr_image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
