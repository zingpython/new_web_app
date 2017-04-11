# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 00:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('image', models.ImageField(upload_to='records')),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('updated', models.DateField(auto_now=True)),
                ('published', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]