# Generated by Django 3.2 on 2021-12-01 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20211130_2050'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoty',
            new_name='Category',
        ),
    ]