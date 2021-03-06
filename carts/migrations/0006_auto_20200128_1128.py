# Generated by Django 2.2 on 2020-01-28 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200127_1348'),
        ('carts', '0005_remove_cart_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='item',
            new_name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='products.Item'),
        ),
    ]
