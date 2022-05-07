# Generated by Django 4.0.2 on 2022-04-24 03:54

import apicalls.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0008_blog_blogsection_mediagroupsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='isPublished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artmediacontent',
            name='mediaFile',
            field=models.ImageField(blank=True, upload_to=apicalls.models.update_media_filename),
        ),
        migrations.AlterField(
            model_name='blogsection',
            name='mediaURL',
            field=models.ImageField(blank=True, upload_to=apicalls.models.update_blog_filename),
        ),
        migrations.AlterField(
            model_name='mediacontent',
            name='mediaFile',
            field=models.ImageField(blank=True, upload_to=apicalls.models.update_project_filename),
        ),
    ]
