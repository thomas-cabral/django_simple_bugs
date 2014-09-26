# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_testcase_teststep'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='title',
            field=models.CharField(default='title', max_length=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='case',
            field=models.ForeignKey(to='cases.Case', related_name='test_cases'),
        ),
        migrations.AlterField(
            model_name='teststep',
            name='test_case',
            field=models.ForeignKey(to='cases.TestCase', related_name='test_steps'),
        ),
    ]
