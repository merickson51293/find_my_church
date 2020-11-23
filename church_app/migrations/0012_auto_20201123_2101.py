# Generated by Django 2.2 on 2020-11-23 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0011_auto_20201123_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='baptist',
            new_name='denomination',
        ),
        migrations.RemoveField(
            model_name='user',
            name='catholic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lutheran',
        ),
        migrations.RemoveField(
            model_name='user',
            name='methodist',
        ),
        migrations.RemoveField(
            model_name='user',
            name='no_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nondenominational',
        ),
        migrations.RemoveField(
            model_name='user',
            name='other',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pentecostal',
        ),
        migrations.RemoveField(
            model_name='user',
            name='reformed',
        ),
    ]
