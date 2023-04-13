# Generated by Django 4.0 on 2023-04-13 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataFlow', '0002_address_remove_project_image_remove_project_pdf_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='DataFlow.address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='DataFlow.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='job_number',
            field=models.IntegerField(null=True),
        ),
    ]
