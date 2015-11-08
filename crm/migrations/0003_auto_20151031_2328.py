# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20151031_2322'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='TypeDon',
        ),
    ]
