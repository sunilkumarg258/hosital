# Generated by Django 2.2 on 2020-04-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='phnum',
            field=models.CharField(default=123456789, max_length=50),
            preserve_default=False,
        ),
    ]
