# Generated by Django 3.2 on 2021-06-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surronshop', '0003_alter_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='none', max_length=50, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='country', max_length=50, verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='email', max_length=30, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='name', max_length=30, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phoneNumber',
            field=models.CharField(default='+7 666 555 44 33', max_length=25, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='zipCode',
            field=models.CharField(default='111 111', max_length=20, verbose_name='Почтоый индекс'),
            preserve_default=False,
        ),
    ]
