# Generated by Django 3.1.1 on 2020-09-30 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0034_auto_20200930_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='pronouns',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='commission',
            name='disclaimer',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
