# Generated by Django 4.2.5 on 2023-12-12 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_person_alter_memodel_options_passport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passport',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_cap', models.CharField(max_length=100)),
                ('post_details', models.CharField(max_length=500)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='first_app.person')),
            ],
        ),
    ]
