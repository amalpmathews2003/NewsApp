# Generated by Django 3.2.8 on 2021-10-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_App', '0004_alter_newsarticle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='type',
            field=models.CharField(choices=[('News', 'News'), ('Local', 'Local'), ('Sprots', 'Sprots'), ('Children', 'Children'), ('Life', 'Life'), ('Tech', 'Tech'), ('Astro', 'Astro'), ('Health', 'Health'), ('Movie', 'Movie'), ('Carrer', 'Carrer'), ('Travel', 'Travel')], default='News', max_length=30),
        ),
    ]
