# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_social_app', '0002_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='blog',
        ),
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
    ]
