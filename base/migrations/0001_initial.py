# Generated by Django 4.1.2 on 2023-04-05 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.users')),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(verbose_name=models.DateTimeField(auto_now_add=True))),
            ],
        ),
        migrations.CreateModel(
            name='Reminders',
            fields=[
                ('id', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('r_date', models.DateTimeField(auto_now_add=True)),
                ('task_id', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='base.tasks')),
            ],
        ),
    ]
