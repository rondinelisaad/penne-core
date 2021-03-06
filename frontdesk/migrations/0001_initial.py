# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('deposited', 'deposited'), ('rejected', 'rejected'), ('accepted', 'accepted')], default='deposited', max_length=100, no_check_for_status=True)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('file', models.FileField(max_length=1024, upload_to='packages/%Y/%m/%d/')),
                ('md5_sum', models.CharField(max_length=32)),
                ('deposit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='package', to='frontdesk.Deposit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
