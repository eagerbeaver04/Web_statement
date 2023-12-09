# Generated by Django 4.2.7 on 2023-12-09 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_corrproffgrop_id_alter_corrsubgroup_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrProffGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.group')),
            ],
        ),
        migrations.CreateModel(
            name='CorrSubjGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.group')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProgress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('attendance', models.BooleanField()),
                ('mark', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CorrProffGrop',
        ),
        migrations.DeleteModel(
            name='CorrSubGroup',
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
        migrations.AlterField(
            model_name='professor',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.group'),
        ),
        migrations.AddField(
            model_name='studentprogress',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.student'),
        ),
        migrations.AddField(
            model_name='studentprogress',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subject'),
        ),
        migrations.AddField(
            model_name='corrproffgroup',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.professor'),
        ),
    ]
