# Generated by Django 3.1.1 on 2020-09-26 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('media', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('materials_used', models.CharField(max_length=100)),
                ('for_sale', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('tw', models.BooleanField(default=False)),
                ('artistId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.artist')),
            ],
        ),
    ]
