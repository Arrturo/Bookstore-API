# Generated by Django 4.1.3 on 2022-12-20 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('last_name',)},
        ),
    ]
