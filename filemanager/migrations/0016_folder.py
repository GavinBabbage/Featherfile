# Generated by Django 4.1 on 2022-09-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0015_files_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foldername', models.CharField(max_length=20)),
            ],
        ),
    ]
