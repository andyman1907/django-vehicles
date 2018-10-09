# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-09 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='brand.Brand'),
        ),
        migrations.AlterUniqueTogether(
            name='vehicle',
            unique_together=set([('enrollment', 'city')]),
        ),
    ]