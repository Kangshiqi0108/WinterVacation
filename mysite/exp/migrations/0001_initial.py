# Generated by Django 4.1.5 on 2023-01-28 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lang',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pub_date', models.DateField()),
                ('inventor', models.CharField(max_length=100)),
                ('application', models.CharField(max_length=200)),
            ],
        ),
    ]
