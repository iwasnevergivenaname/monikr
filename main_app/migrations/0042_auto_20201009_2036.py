# Generated by Django 3.1.1 on 2020-10-09 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0041_auto_20201009_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='contact',
            name='email_address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
