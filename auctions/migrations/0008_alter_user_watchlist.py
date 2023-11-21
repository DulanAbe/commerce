# Generated by Django 4.1.5 on 2023-11-20 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_user_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, related_name='Interested_users', to='auctions.listing'),
        ),
    ]