# Generated by Django 3.0.3 on 2020-02-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_item_update_defaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='featured',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
