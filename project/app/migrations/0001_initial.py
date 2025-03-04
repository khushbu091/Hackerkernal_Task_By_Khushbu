# Generated by Django 5.0.6 on 2024-07-03 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('MOBILE', models.IntegerField()),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_details', models.TextField(max_length=50)),
                ('Task_type', models.CharField(choices=[('Pending', 'pending'), ('Done', 'done')], max_length=50)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
