# Generated by Django 4.2.7 on 2023-12-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_markcell_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subjects',
            field=models.ManyToManyField(default=None, related_name='professors', to='main.subject'),
        ),
    ]
