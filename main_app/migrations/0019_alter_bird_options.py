# Generated by Django 4.1 on 2022-08-26 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_alter_bird_options_alter_bird_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bird',
            options={'ordering': ['-date']},
        ),
    ]
