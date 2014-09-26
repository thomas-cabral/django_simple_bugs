# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalRequirement',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('detail', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True, editable=False)),
                ('updated_on', models.DateTimeField(blank=True, editable=False)),
                ('user_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('changed_by_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('project_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'historical requirement',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=55)),
                ('detail', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('changed_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='requirement_changed_by', null=True)),
                ('project', models.ForeignKey(related_name='requirement_project', to='projects.Project')),
                ('user', models.ForeignKey(related_name='requirements_user', to=settings.AUTH_USER_MODEL)),
                ('working_on', models.ManyToManyField(related_name='working_on', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
            bases=(models.Model,),
        ),
    ]
