# Generated by Django 3.0.8 on 2020-08-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0005_auto_20200811_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
