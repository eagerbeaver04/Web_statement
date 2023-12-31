# Generated by Django 4.2.7 on 2023-12-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(default=None, max_length=100)),
                ('last_name', models.CharField(default=None, max_length=100)),
                ('middle_name', models.CharField(default=None, max_length=100)),
                ('gender', models.CharField(default=None, max_length=10)),
                ('age', models.IntegerField(default=None)),
                ('role', models.CharField(choices=[('ST', 'Student'), ('PR', 'Professor')], default='ST', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='corrproffgroup',
            name='group',
        ),
        migrations.RemoveField(
            model_name='corrproffgroup',
            name='professor',
        ),
        migrations.RemoveField(
            model_name='corrsubjgroup',
            name='group',
        ),
        migrations.RemoveField(
            model_name='corrsubjgroup',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.RemoveField(
            model_name='studentprogress',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentprogress',
            name='subject',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='number',
            new_name='name',
        ),
        migrations.AddField(
            model_name='group',
            name='subjects',
            field=models.ManyToManyField(to='main.subject'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='CorrProffGroup',
        ),
        migrations.DeleteModel(
            name='CorrSubjGroup',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentProgress',
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.group'),
        ),
        migrations.AddField(
            model_name='progress',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
        migrations.AddField(
            model_name='progress',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='professors',
            field=models.ManyToManyField(to='main.user'),
        ),
    ]
