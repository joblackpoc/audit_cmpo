# Generated by Django 4.0.6 on 2022-07-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_document_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
