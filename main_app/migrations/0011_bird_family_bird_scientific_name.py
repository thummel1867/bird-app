# Generated by Django 4.1 on 2022-08-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_bird_remove_article_author_delete_topic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='family',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='scientific_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
