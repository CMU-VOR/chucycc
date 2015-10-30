# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice_work_order', '0002_auto_20151027_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='session',
            field=models.ForeignKey(default='', to='voice_work_order.Session'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='customer',
            field=models.OneToOneField(to='voice_work_order.Customer'),
        ),
        migrations.AlterField(
            model_name='session',
            name='plane',
            field=models.OneToOneField(to='voice_work_order.Plane'),
        ),
    ]
