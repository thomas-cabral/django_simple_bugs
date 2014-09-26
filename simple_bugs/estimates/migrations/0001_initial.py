# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=55, choices=[('ENGINEERING', 'Engineering'), ('PRODUCTION_QA', 'Production QA')])),
                ('estimate', models.PositiveIntegerField(blank=True, null=True)),
                ('total_time', models.PositiveIntegerField(blank=True, null=True)),
                ('case', models.ForeignKey(related_name='case_estimate', to='cases.Case')),
                ('user', models.ForeignKey(related_name='estimate_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
