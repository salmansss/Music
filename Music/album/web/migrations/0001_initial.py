# Generated by Django 3.0.1 on 2020-01-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('albums_id', models.AutoField(primary_key=True, serialize=False)),
                ('albums_name', models.CharField(max_length=200)),
                ('albums_year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songs_name', models.CharField(max_length=200)),
                ('songs_year', models.DateTimeField()),
                ('songs_singer', models.CharField(max_length=200)),
            ],
        ),
    ]
