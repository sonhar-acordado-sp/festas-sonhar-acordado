# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traininglocal',
            name='complement',
            field=models.CharField(verbose_name='Complement', max_length=32, blank=True),
        ),
    ]
