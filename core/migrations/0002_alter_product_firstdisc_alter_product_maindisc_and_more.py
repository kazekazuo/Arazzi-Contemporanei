# Generated by Django 4.2 on 2023-04-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='firstDisc',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='mainDisc',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondDisc',
            field=models.TextField(max_length=255),
        ),
    ]
