# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AddField(
            model_name='book',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AddField(
            model_name='cover',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='cover',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cover',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AddField(
            model_name='publishinghouse',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='publishinghouse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publishinghouse',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=127, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=127, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Cover', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=1024, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=127, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=1, verbose_name='Pages'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.PublishingHouse', verbose_name='Publishing house'),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='cover',
            name='name',
            field=models.CharField(max_length=127, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]
