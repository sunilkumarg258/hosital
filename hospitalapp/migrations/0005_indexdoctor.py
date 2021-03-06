# Generated by Django 2.2 on 2020-04-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0004_auto_20200422_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('specification', models.CharField(max_length=100)),
            ],
        ),
    ]
