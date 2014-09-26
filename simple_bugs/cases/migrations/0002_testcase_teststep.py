# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.TextField()),
                ('case', models.ForeignKey(to='cases.Case', related_name='master_case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestStep',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=55)),
                ('data', models.TextField()),
                ('test_case', models.ForeignKey(to='cases.TestCase', related_name='master_test')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
