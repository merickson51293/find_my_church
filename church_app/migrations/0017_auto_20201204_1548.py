# Generated by Django 2.2 on 2020-12-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0016_auto_20201201_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpic',
            name='user_Img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
