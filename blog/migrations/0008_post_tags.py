# Generated by Django 3.1.6 on 2021-04-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='blog.Tag'),
        ),
    ]
