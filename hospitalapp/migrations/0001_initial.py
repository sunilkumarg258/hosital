# Generated by Django 2.2 on 2020-04-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('dname', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
