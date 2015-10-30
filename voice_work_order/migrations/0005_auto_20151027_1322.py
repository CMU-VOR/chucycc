# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice_work_order', '0004_workorder_ordertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='radio',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C')]),
        ),
    ]
