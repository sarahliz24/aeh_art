# Generated by Django 3.2 on 2023-11-13 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
        ('wishlist', '0006_rename_artwork_id_wishlist_artwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion. 
                                    CASCADE, to='products.product'),
        ),
    ]
