# Generated by Django 5.0.4 on 2024-05-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0006_remove_news_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
