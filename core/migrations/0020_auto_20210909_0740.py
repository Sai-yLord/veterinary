# Generated by Django 3.2.5 on 2021-09-09 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_products_star'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
