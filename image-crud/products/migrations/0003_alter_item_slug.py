# Generated by Django 4.1.3 on 2022-11-21 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_item_options_item_slug_item_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
