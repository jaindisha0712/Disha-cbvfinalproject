# Generated by Django 3.0.6 on 2020-06-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('colour', models.CharField(max_length=256)),
                ('taste', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
