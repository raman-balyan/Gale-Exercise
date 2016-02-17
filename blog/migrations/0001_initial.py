# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=50)),
                ('limited_content', models.CharField(max_length=400)),
                ('full_content', models.TextField()),
            ],
        ),
    ]
