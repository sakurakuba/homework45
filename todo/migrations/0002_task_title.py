# Generated by Django 4.0.6 on 2022-07-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='no task name', max_length=300, verbose_name='title'),
        ),
    ]