# Generated by Django 3.2.18 on 2023-04-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='user_images/%Y/%m/%d/'),
        ),
    ]
