# Generated by Django 4.0 on 2022-01-04 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_description_product_description_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description_en',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_en',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title_en',
            new_name='title',
        ),
    ]
