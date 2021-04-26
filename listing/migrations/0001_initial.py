# Generated by Django 3.1.6 on 2021-03-31 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import listing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('address', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.FileField(upload_to=listing.models.user_media_path)),
                ('rating', models.FloatField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListingCategory',
            fields=[
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
                ('likes', models.IntegerField(default=0)),
                ('icon', models.FileField(blank=True, null=True, upload_to='listing_icon/')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('rated', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_rating', to='listing.listing')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='rated by')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_categ', to='listing.listingcategory'),
        ),
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='user_wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
