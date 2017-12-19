# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scotstartup', '0004_auto_20170830_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='featured',
            field=models.BooleanField(default=b'false'),
            preserve_default=True,
        ),
    ]
