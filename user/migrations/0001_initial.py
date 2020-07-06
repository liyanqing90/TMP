# Generated by Django 3.0.7 on 2020-07-05 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('category', models.CharField(max_length=10)),
                ('owner', models.CharField(max_length=10)),
                ('finish', models.IntegerField(choices=[(0, '执行中'), (1, '已归档')], default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Project')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Status')),
            ],
        ),
    ]