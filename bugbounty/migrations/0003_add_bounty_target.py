# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 22:17
from __future__ import unicode_literals

import bugbounty.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugbounty', '0002_add_dates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('details', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('owners', models.ManyToManyField(related_name='owned_bounty_targets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=enumfields.fields.EnumField(default='new', enum=bugbounty.models.ReportStatus, max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='bugbounty.Target'),
        ),
    ]