# Generated by Django 4.1.2 on 2022-11-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-05-24'),
            preserve_default=False,
        ),
    ]
