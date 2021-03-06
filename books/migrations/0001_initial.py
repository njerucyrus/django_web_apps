# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('copies', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='bks_photos')),
                ('publisher', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('book_title',),
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookReturnHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_reg_no', models.CharField(max_length=100)),
                ('student_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone Number')),
                ('book_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('date_returned', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date_returned',),
                'verbose_name_plural': 'Books Returned Log',
            },
        ),
        migrations.CreateModel(
            name='BooksIssued',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_reg_no', models.CharField(max_length=100)),
                ('student_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone Number')),
                ('book_title', models.CharField(max_length=100)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('exp_return_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('date_issued',),
                'verbose_name_plural': 'Books Issued',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='book_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.BookCategory'),
        ),
    ]
