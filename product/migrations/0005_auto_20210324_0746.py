# Generated by Django 3.1.7 on 2021-03-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210323_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='caption',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery_toshkent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery_uzb',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='guarentee',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Kafolat: '),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='caption',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
