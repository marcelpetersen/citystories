# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20160121_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
