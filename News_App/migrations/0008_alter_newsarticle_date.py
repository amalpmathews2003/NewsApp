# Generated by Django 3.2.8 on 2021-10-21 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_App', '0007_auto_20211021_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
