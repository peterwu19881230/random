# Generated by Django 3.0.3 on 2020-02-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_name', models.CharField(max_length=100)),
                ('st_class', models.CharField(max_length=20)),
                ('st_sex', models.CharField(max_length=20)),
                ('st_mark', models.IntegerField()),
            ],
        ),
    ]
