# Generated by Django 3.0.3 on 2020-02-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20200210_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['order', '-start_date', 'end_date']},
        ),
        migrations.AddField(
            model_name='slider',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
