# Generated by Django 3.0.3 on 2020-02-10 07:22

from django.db import migrations, models
import marketing.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=marketing.models.slider_upload)),
                ('header_text', models.CharField(blank=True, max_length=120, null=True)),
                ('text', models.CharField(blank=True, max_length=120, null=True)),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-start_date', 'end_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='marketingmessage',
            options={'ordering': ['-start_date', 'end_date']},
        ),
    ]
