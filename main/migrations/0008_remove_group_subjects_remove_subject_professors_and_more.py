# Generated by Django 4.2.7 on 2023-12-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_progress_user_remove_corrproffgroup_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='subjects',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='professors',
        ),
        migrations.AddField(
            model_name='user',
            name='subjects',
            field=models.ManyToManyField(to='main.subject'),
        ),
    ]
