# Generated by Django 3.2.7 on 2021-10-02 08:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_article_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
