# Generated by Django 3.1.5 on 2021-01-12 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lost_input',
            options={'ordering': ('-registered_date',), 'verbose_name': '분실물', 'verbose_name_plural': '분실물들'},
        ),
    ]
