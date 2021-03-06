# Generated by Django 3.1.7 on 2021-03-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210323_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
