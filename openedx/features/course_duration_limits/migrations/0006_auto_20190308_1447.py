# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-08 14:47
from __future__ import absolute_import, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_duration_limits', '0005_auto_20190306_1546'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='coursedurationlimitconfig',
            index=models.Index(fields=['site', 'org', 'course'], name='course_dura_site_id_424016_idx'),
        ),
    ]
