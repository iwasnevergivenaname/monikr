# Generated by Django 3.1.1 on 2020-10-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0038_auto_20201001_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='as_color',
            field=models.CharField(default='black', max_length=50),
        ),
    ]
