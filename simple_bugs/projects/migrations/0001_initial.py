# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=55)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('group', models.ForeignKey(related_name='project_group', to='groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
