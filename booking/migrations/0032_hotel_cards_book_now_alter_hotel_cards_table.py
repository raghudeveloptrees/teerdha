# Generated by Django 4.2.7 on 2024-05-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0031_navbar_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_cards',
            name='Book_now',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterModelTable(
            name='hotel_cards',
            table=None,
        ),
    ]