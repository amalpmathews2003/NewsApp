# Generated by Django 3.2.8 on 2021-10-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_App', '0015_alter_newsarticle_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='type',
            field=models.CharField(choices=[('Top News', 'Top News'), ('News', 'News'), ('Local', 'Local'), ('Sprots', 'Sprots'), ('Children', 'Children'), ('Life', 'Life'), ('Tech', 'Tech'), ('Astro', 'Astro'), ('Health', 'Health'), ('Movie', 'Movie'), ('Carrer', 'Carrer'), ('Travel', 'Travel')], default='News', max_length=30),
        ),
    ]
