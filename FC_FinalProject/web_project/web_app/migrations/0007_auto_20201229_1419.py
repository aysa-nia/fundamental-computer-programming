# Generated by Django 3.1.4 on 2020-12-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_user_uploadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uploadimage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
