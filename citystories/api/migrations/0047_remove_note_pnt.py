# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_note_pnt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='pnt',
        ),
    ]
