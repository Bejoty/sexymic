# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0003_auto_20141224_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='featured_game',
            field=models.ForeignKey(to='stream.Game', null=True),
        ),
    ]
