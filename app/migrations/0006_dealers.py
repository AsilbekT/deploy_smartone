# Generated by Django 4.0 on 2022-01-13 08:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_textstotranslate_text_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('working_days', tinymce.models.HTMLField()),
            ],
        ),
    ]
