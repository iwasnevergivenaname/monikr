# Generated by Django 3.1.1 on 2020-10-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0040_auto_20201009_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
    ]
