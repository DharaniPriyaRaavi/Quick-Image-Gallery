# Generated by Django 4.1.3 on 2022-11-23 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Email',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='member',
            name='Password',
            field=models.CharField(default='Test@123', max_length=300),
        ),
        migrations.AddField(
            model_name='member',
            name='Password_confirmation',
            field=models.CharField(default='Test@123', max_length=300),
        ),
        migrations.AddField(
            model_name='member',
            name='Username',
            field=models.CharField(default='Test', max_length=300),
        ),
    ]
