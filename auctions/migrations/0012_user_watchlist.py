# Generated by Django 4.1.5 on 2023-11-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_user_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='Interested_users', to='auctions.listing'),
        ),
    ]
