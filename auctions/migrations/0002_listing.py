# Generated by Django 4.1.5 on 2023-07-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=300)),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=7)),
                ('url', models.CharField(blank=True, max_length=300)),
                ('category', models.CharField(choices=[('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Home', 'Home')], max_length=11)),
            ],
        ),
    ]
