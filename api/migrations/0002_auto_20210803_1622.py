# Generated by Django 3.2.6 on 2021-08-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoris',
            name='display_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='favoris',
            name='display_phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='favoris',
            name='image_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='favoris',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='favoris',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]