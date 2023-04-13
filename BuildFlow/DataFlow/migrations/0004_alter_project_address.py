# Generated by Django 4.0 on 2023-04-13 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataFlow', '0003_project_address_alter_address_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='DataFlow.address'),
        ),
    ]
