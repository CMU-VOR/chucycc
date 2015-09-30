# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voiceapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='query',
        ),
        migrations.AddField(
            model_name='query',
            name='result',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
