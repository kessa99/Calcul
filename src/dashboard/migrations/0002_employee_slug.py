# Generated by Django 4.2.5 on 2023-10-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.SlugField(default='', max_length=64),
            preserve_default=False,
        ),
    ]