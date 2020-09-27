# Generated by Django 3.1.1 on 2020-09-27 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_artist_bg_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=100)),
                ('content', models.CharField(default='write it out here', max_length=100)),
                ('materials_used', models.CharField(default='materials', max_length=100)),
                ('for_sale', models.BooleanField()),
            ],
        ),
    ]
