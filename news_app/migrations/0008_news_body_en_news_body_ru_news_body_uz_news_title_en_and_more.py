# Generated by Django 5.0.4 on 2024-05-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0007_category_name_en_category_name_ru_category_name_uz'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
