# Generated by Django 4.1.5 on 2023-11-20 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_user_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.ForeignKey(default='Empty', on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]
