# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('nome_empresa', models.CharField(max_length=50)),
            ],
        ),
    ]