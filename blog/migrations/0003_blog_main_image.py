# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150620_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='main_image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
    ]
