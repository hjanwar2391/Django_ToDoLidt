# Generated by Django 4.2.3 on 2023-08-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_alter_todomodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
