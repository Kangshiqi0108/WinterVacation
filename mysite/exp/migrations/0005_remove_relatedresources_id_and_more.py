# Generated by Django 4.1.5 on 2023-03-31 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0004_relatedresources_researchresults_student_delete_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatedresources',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='admissiondate',
        ),
        migrations.AlterField(
            model_name='relatedresources',
            name='link',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]
