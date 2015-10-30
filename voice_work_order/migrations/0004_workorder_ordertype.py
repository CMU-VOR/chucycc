# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice_work_order', '0003_auto_20151027_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='ordertype',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
