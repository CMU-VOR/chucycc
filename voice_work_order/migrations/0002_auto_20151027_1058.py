# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice_work_order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plane',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='name',
        ),
    ]
