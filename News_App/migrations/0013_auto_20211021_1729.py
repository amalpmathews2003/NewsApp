# Generated by Django 3.2.8 on 2021-10-21 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News_App', '0012_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name_plural': 'Tags'},
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='href',
            field=models.URLField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='newsArticle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='News_App.newsarticle'),
        ),
    ]