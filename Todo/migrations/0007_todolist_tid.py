# Generated by Django 3.0.8 on 2020-08-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0006_auto_20200811_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='tid',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
