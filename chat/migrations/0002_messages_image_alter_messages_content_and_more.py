# Generated by Django 4.0.4 on 2022-11-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chats/'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]