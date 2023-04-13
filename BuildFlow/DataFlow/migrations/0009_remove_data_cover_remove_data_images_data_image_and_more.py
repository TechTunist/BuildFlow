# Generated by Django 4.1 on 2023-04-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataFlow', '0008_remove_data_image_data_cover_data_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='data',
            name='images',
        ),
        migrations.AddField(
            model_name='data',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='data',
            name='pdf_file',
            field=models.FileField(null=True, upload_to='pdfs/'),
        ),
    ]
