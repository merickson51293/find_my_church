# Generated by Django 2.2 on 2020-12-07 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0002_auto_20201205_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='church_app.Church')),
            ],
        ),
    ]
