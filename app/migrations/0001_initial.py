# Generated by Django 3.1.3 on 2021-01-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('rnum', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=4)),
                ('age', models.IntegerField()),
                ('co_survey', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'survey',
                'managed': False,
            },
        ),
    ]
