# Generated by Django 4.0.6 on 2022-07-15 12:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_document_content_alter_document_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='คำอธิบายเนื้อหาอย่างละเอียด'),
        ),
    ]
