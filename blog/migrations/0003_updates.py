# Generated by Django 3.0.5 on 2020-09-25 07:28

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200924_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
