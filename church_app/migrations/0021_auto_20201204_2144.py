# Generated by Django 2.2 on 2020-12-04 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0020_churchcomments_usercomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('user_type', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('church', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='church_message', to='church_app.Church')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_message', to='church_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='user',
        ),
        migrations.AlterField(
            model_name='churchcomments',
            name='wall_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='church_post_comments', to='church_app.Message'),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='wall_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post_comments', to='church_app.Message'),
        ),
        migrations.DeleteModel(
            name='ChurchMessage',
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
    ]