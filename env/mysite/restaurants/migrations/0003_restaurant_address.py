# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_remove_restaurant_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
