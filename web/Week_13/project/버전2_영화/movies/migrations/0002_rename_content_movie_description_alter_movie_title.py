# Generated by Django 4.2.11 on 2024-04-05 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='content',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
