# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dons',
            old_name='type',
            new_name='type_don',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='type',
            new_name='type_don',
        ),
    ]
