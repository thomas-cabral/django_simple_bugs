# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requirements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(default='BUG', max_length=155, choices=[('BUG', 'Bug'), ('FEATURE_REQUEST', 'Feature Request')])),
                ('title', models.CharField(max_length=55)),
                ('detail', models.TextField()),
                ('closed', models.BooleanField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='assigned', null=True)),
                ('changed_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='case_changed_by', null=True)),
                ('project', models.ForeignKey(related_name='case_project', to='projects.Project')),
                ('requirement', models.ForeignKey(blank=True, verbose_name='Related Requirement', to='requirements.Requirement', related_name='requirement', null=True)),
                ('user', models.ForeignKey(related_name='case_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalCase',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('type', models.CharField(default='BUG', max_length=155, choices=[('BUG', 'Bug'), ('FEATURE_REQUEST', 'Feature Request')])),
                ('title', models.CharField(max_length=55)),
                ('detail', models.TextField()),
                ('closed', models.BooleanField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, editable=False)),
                ('updated_on', models.DateTimeField(blank=True, editable=False)),
                ('user_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('changed_by_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('assigned_to_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('requirement_id', models.IntegerField(blank=True, db_index=True, verbose_name='Related Requirement', null=True)),
                ('project_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'historical case',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
    ]
