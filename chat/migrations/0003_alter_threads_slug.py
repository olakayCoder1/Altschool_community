# Generated by Django 4.0.4 on 2022-11-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_messages_image_alter_messages_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threads',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
