# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_social_app', '0003_auto_20170903_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='email',
        ),
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(default=12, to='django_social_app.Blogs'),
            preserve_default=False,
        ),
    ]
