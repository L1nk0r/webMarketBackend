# Generated by Django 3.2 on 2021-06-24 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surronshop', '0005_handmadeorder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='final_price',
            new_name='total_price',
        ),
    ]