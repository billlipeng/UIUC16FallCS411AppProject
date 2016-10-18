# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=1900)),
                ('cast', models.CharField(max_length=200)),
                ('rating', models.FloatField(default=0.0)),
                ('genre', models.CharField(max_length=200)),
                ('cover', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MovieLocR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc_id', to='moviefun.Movie')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_id', to='moviefun.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='RecomR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie1_id', to='moviefun.Movie')),
                ('movie2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie2_id', to='moviefun.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='TVPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('season_number', models.IntegerField(default=0)),
                ('episode_number', models.IntegerField(default=0)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviefun.Movie')),
            ],
        ),
    ]
