# Generated by Django 3.1.2 on 2020-10-22 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20201022_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistrationmodel',
            name='date_of_birth',
        ),
    ]
