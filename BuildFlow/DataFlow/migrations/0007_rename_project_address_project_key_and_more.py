# Generated by Django 4.0 on 2023-04-13 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataFlow', '0006_remove_project_client_project_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='project',
            new_name='project_key',
        ),
        migrations.AddField(
            model_name='project',
            name='project_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DataFlow.address'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DataFlow.data'),
        ),
    ]
