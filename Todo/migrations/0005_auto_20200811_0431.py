# Generated by Django 3.0.8 on 2020-08-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0004_auto_20200811_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(default='johnnydoe@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='John Doe', max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='salutation',
            field=models.CharField(default='Mr', max_length=10),
        ),
    ]
