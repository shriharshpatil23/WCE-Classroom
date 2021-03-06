# Generated by Django 3.1.3 on 2022-05-05 09:58

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('video', models.FileField(blank=True, null=True, upload_to=base.models.filepath)),
            ],
        ),
    ]
