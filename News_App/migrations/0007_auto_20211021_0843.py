# Generated by Django 3.2.8 on 2021-10-21 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_App', '0006_newsarticle_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
