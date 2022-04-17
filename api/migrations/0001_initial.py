# Generated by Django 3.2.7 on 2022-04-17 06:18

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=78)),
                ('body', models.CharField(max_length=40000)),
                ('send_on', models.DateTimeField(default=datetime.datetime.today)),
                ('recipients_list', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=255), size=None)),
                ('attachment_file', models.FileField(blank=True, null=True, upload_to='mail/uploads/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
