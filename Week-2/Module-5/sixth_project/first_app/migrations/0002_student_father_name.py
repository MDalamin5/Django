# Generated by Django 4.2.5 on 2023-12-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='No Name'),
        ),
    ]
