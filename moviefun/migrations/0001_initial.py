# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 02:41
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
                ('address', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('longitude', models.CharField(default='N/A', max_length=200)),
                ('latitude', models.CharField(default='N/A', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('imdbid', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('title', models.CharField(default='N/A', max_length=200)),
                ('year', models.CharField(default='N/A', max_length=200)),
                ('rated', models.CharField(default='N/A', max_length=200)),
                ('released', models.CharField(default='N/A', max_length=200)),
                ('runtime', models.CharField(default='N/A', max_length=200)),
                ('genre', models.CharField(default='N/A', max_length=200)),
                ('director', models.CharField(default='N/A', max_length=200)),
                ('writer', models.CharField(default='N/A', max_length=200)),
                ('actors', models.CharField(default='N/A', max_length=200)),
                ('plot', models.CharField(default='N/A', max_length=500)),
                ('language', models.CharField(default='N/A', max_length=200)),
                ('awards', models.CharField(default='N/A', max_length=200)),
                ('poster', models.CharField(default='N/A', max_length=200)),
                ('imdbrating', models.CharField(default='N/A', max_length=200)),
                ('imdbvotes', models.CharField(default='N/A', max_length=200)),
                ('type', models.CharField(default='N/A', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RecomR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MovieLocR',
            fields=[
                ('imdbid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='moviefun.Movie')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviefun.Loc')),
            ],
        ),
        migrations.CreateModel(
            name='TVPlay',
            fields=[
                ('imdbid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='moviefun.Movie')),
                ('season', models.CharField(default='N/A', max_length=200)),
                ('episode', models.CharField(default='N/A', max_length=200)),
                ('seriesid', models.CharField(default='N/A', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TVSeries',
            fields=[
                ('seriesid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='moviefun.Movie')),
                ('totalseasons', models.CharField(default='N/A', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='recomr',
            name='movie1_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie1_id', to='moviefun.Movie'),
        ),
        migrations.AddField(
            model_name='recomr',
            name='movie2_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie2_id', to='moviefun.Movie'),
        ),
    ]
