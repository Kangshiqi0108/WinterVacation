# Generated by Django 4.1.5 on 2023-02-18 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0002_lang_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lang',
            name='intro',
            field=models.TextField(),
        ),
    ]
