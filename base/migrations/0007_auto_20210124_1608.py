# Generated by Django 3.0.5 on 2021-01-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/defult.jpg', null=True, upload_to='imgs'),
        ),
    ]
