# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flattexts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatTextTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('content', models.TextField(verbose_name='content')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='flattexts.FlatText', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'flattexts_flattext_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'flat text Translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='flattexttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.RemoveField(
            model_name='flattext',
            name='content',
        ),
    ]
