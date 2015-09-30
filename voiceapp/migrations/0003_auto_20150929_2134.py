# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voiceapp', '0002_auto_20150923_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Query',
        ),
        migrations.AddField(
            model_name='content',
            name='keyword',
            field=models.ManyToManyField(to='voiceapp.Keyword'),
        ),
    ]
