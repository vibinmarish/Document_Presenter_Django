# Generated by Django 3.0.7 on 2020-06-13 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_auto_20200613_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='Document',
        ),
    ]