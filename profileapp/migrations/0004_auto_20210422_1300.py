# Generated by Django 3.2 on 2021-04-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_auto_20210422_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contacts',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='edit_ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]