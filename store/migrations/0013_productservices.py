# Generated by Django 4.0 on 2022-01-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_description_en_product_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('name_uz', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('title_uz', models.CharField(max_length=200, null=True)),
                ('description_ru', models.TextField(default='description')),
                ('description_uz', models.TextField(default='description')),
                ('description', models.TextField(default='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='uploads/')),
                ('image2', models.ImageField(default='default.jpg', upload_to='uploads/')),
                ('image3', models.ImageField(default='default.jpg', upload_to='uploads/')),
                ('image4', models.ImageField(default='default.jpg', upload_to='uploads/')),
                ('image5', models.ImageField(default='default.jpg', upload_to='uploads/')),
            ],
        ),
    ]
